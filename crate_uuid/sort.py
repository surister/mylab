from crate_uuid.uuid import uuid7
import base64
from random import shuffle

from normalb64 import to_base64n

# Check that uuid7 is sortable on hex32 and a custom base64 encoding but not in RFC base64.
# https://gist.github.com/getumen/dbdcb349ab55700fac4a3bf731d8bcab

def is_sorted(arr, i_sort: int) -> bool:
    """returns whether the given `arr` is sorted or not"""
    for i in range(len(arr) - 1):
        if not arr[i][i_sort] < arr[i + 1][i_sort]:
            return False
    return True


if __name__ == '__main__':
    base = []
    hex32 = []
    orderedBase = []

    for i in range(10_000):
        t = uuid7() # Change here what you want to test.

        base.append((i, base64.urlsafe_b64encode(t.bytes).decode('utf-8').rstrip('=')))
        hex32.append((i, base64.b32hexencode(t.bytes).decode('utf-8').rstrip('=')))
        orderedBase.append((i, to_base64n(t.bytes, pad=False)))

    shuffle(base)
    shuffle(hex32)
    shuffle(orderedBase)

    print('Original (Shuffled):')
    print('is base64 sorted', is_sorted(base, 0))
    print('is hex32 sorted', is_sorted(hex32, 0))
    print('is ordered base64 sorted', is_sorted(orderedBase, 0))

    base.sort(key=lambda x: x[1])
    hex32.sort(key=lambda x: x[1])
    orderedBase.sort(key=lambda x: x[1])

    print('Sorted:')
    print('is base64 sorted', is_sorted(base, 0))
    print('is hex32 sorted', is_sorted(hex32, 0))
    print('is ordered base64 sorted', is_sorted(orderedBase, 0))
