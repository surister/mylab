import json
import time

import psutil

t00 = time.time()
running = True

import subprocess

file = '/home/surister/PycharmProjects/lab/mytlab/code/load_parquet_blog/load_parquet1.py'
exec_path = '/home/surister/.cache/pypoetry/virtualenvs/mytlab-3ZSRO7bn-py3.12/bin/python' + ' ' + file

print(f'Running: {exec_path}')
proc = subprocess.Popen(exec_path, shell=True)

time.sleep(.5)  # Let processes if spawned, start.

proc = psutil.Process(proc.pid)
procs = [proc, *proc.children(recursive=True)]


class StatsTracker:
    def __init__(self):
        self.upload_mbs = []
        self.cpu_usage_percentage = []
        self.mem_mb = []
        self.time = []
        self.t0 = time.time()

    def add_step(self, *, upload_mbs, cpu_usage_percentage, mem_mb):
        self.upload_mbs.append(upload_mbs)
        self.cpu_usage_percentage.append(cpu_usage_percentage)
        self.mem_mb.append(mem_mb)
        self.time.append(time.time())

    def chartsjs_format(self):
        """
        Returns the format for charts.js, to simply copypaste.
        """
        self.cpu_usage_percentage[0] = 0.0
        obj = {
            'labels': self.time,
            'datasets': [
                {
                    'data': self.mem_mb,
                    'borderColor': 'rgb(255, 99, 132)',
                    'label': 'Memory (Gb)',
                    'color': 'white',
                },
                {
                    'data': self.upload_mbs,
                    'borderColor': 'rgb(54, 162, 235)',
                    'label': 'Upload speed (Mb/s)',
                },
                {
                    'data': self.cpu_usage_percentage,
                    'borderColor': 'rgb(255, 205, 86)',
                    'label': 'CPU (%)'
                }
            ]
        }
        return json.dumps(obj)


def avg(it):
    """
    Returns the average of the iterable
    """
    return sum(it) / (len(it))


def get_updown(interface: str) -> tuple:
    io = psutil.net_io_counters(pernic=True)[interface]
    return io[0], io[1]


# try:
#     proc = list(filter(lambda x: x.name() == 'firefox', psutil.process_iter()))[0]
# except IndexError:
#     raise Exception("No programm is being run")

ul = 0.00
dl = 0.00
t0 = time.time()
stats_tracker: StatsTracker = StatsTracker()

updown = get_updown('enp5s0')

print("Getting statistics! Everything is working; see you in a bit.")
for p in procs:
    print(f'Getting statistics for Process: {p.name()} pid: {p.pid}')

try:
    while running:
        if not procs[0].is_running():
            break

        last_up_down = updown
        t1 = time.time()
        updown = get_updown('enp5s0')

        try:
            ul, dl = [
                (now - last) / (t1 - t0) / (1024.0 ** 2)
                for now, last in zip(updown, last_up_down)
            ]
            t0 = time.time()
        except:
            pass

        cpu_percent = psutil.cpu_percent(interval=1)
        mem = sum(map(lambda _proc: _proc.memory_info().rss / (1024 ** 2), procs))

        iocount = proc.io_counters()

        stats_tracker.add_step(
            upload_mbs=round(ul, 2),
            cpu_usage_percentage=cpu_percent,
            mem_mb=round(mem / 1024, 2)
        )
        # print("UL: {:0.2f} mB/s \n".format(ul))  # + "DL: {:0.2f} mB/s".format(dl))
        # print(f"CPU Usage: {cpu_percent}%")
        # print(f"Mem: {mem:.2f}MB")


except (KeyboardInterrupt, psutil.AccessDenied, psutil.NoSuchProcess):
    pass

finally:
    print(f"Gathered {len(stats_tracker.time)} metrics")

    rows = 2_964_624
    executed_file = open(file).read()
    print("\n")
    print(
        f'''
::Editor{{lang="python" header_text="load_parquet1.py" show_header=true}}
<pre>{executed_file}</pre>
::        

Results
'''
    )
    print(f'* Time: [{time.time() - t00:.2f}s]{{.h}}')
    print(
        f'* Avg upload speed: [{round(avg(stats_tracker.upload_mbs), 2)}Mb/s]{{.h}} - [max({max(stats_tracker.upload_mbs)})]{{.h}}')
    print(
        f'* Avg memory usage: [{round(avg(stats_tracker.mem_mb), 2)}Gb]{{.h}} - [max({max(stats_tracker.mem_mb)})]{{.h}}')
    print(
        f'* Avg cpu usage: [{round(avg(stats_tracker.cpu_usage_percentage), 2)}%]{{.h}} - [max({max(stats_tracker.cpu_usage_percentage)})]{{.h}}')
    print(
        f'* Avg throughput: {rows} rows / {time.time() - t00:.2f} = [{round(rows / (time.time() - t00), 2)}rows/s]{{.h}}')
    print(f'''
::line{{.pt-5}}
---
"chartProps": {stats_tracker.chartsjs_format()}
---
::
''')
