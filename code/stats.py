import datetime
import time

import psutil

running = True
proc: psutil.Process | None = None


class StatsTracker:
    def __init__(self):
        self.upload_mbs = []
        self.cpu_usage_percentage = []
        self.mem_mb = []
        self.time = []

    def add_step(self, *, upload_mbs, cpu_usage_percentage, mem_mb):
        self.upload_mbs.append(upload_mbs)
        self.cpu_usage_percentage.append(cpu_usage_percentage)
        self.mem_mb.append(mem_mb)
        self.time.append(str(datetime.datetime.now()))


def get_updown(interface: str) -> tuple:
    io = psutil.net_io_counters(pernic=True)[interface]
    return io[0], io[1]


try:
    proc = list(filter(lambda x: x.name() == 'firefox', psutil.process_iter()))[0]
except IndexError:
    raise Exception("No programm is being run")

ul = 0.00
dl = 0.00
t0 = time.time()
stats_tracker = StatsTracker()

updown = get_updown('enp5s0')

try:
    while running:
        if not proc.is_running():
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
        mem = proc.memory_info().rss / (1024 ** 2)
        iocount = proc.io_counters()

        stats_tracker.add_step(
            upload_mbs=f'{ul:.2f}',
            cpu_usage_percentage=cpu_percent,
            mem_mb=f'{mem:.2f}'
        )
        # print("UL: {:0.2f} mB/s \n".format(ul))  # + "DL: {:0.2f} mB/s".format(dl))
        # print(f"CPU Usage: {cpu_percent}%")
        # print(f"Mem: {mem:.2f}MB")

        time.sleep(1)

except psutil.NoSuchProcess:
    pass
