"""
Results of k_ordered_flake.json:
---------------------------
Before shuffling
is sorted elasticflakes: True
is sorted hex_elasticflakes: True
After shuffling
is sorted elasticflakes: False
is sorted hex_elasticflakes: False
551
after sorting
is sorted elasticflakes: False
is sorted hex_elasticflakes: True


Results of elasticflakes.json
-----------------------------
Before shuffling
is sorted elasticflakes: True
is sorted hex_elasticflakes: True
After shuffling
is sorted elasticflakes: False
is sorted hex_elasticflakes: False
after sorting
is sorted elasticflakes: False
is sorted hex_elasticflakes: False
"""

import base64
import json

from crate_uuid.sort import is_sorted

import random

# Proves that elasticflakes are not ordered.

# k_ordered_flake.json is the new elasticsearch flake k-ordered flake
# elasticflakes.json is the classic not k_ordereded elasticflake (Used in CrateDB)

with open('elasticflakes.json') as f:
    elasticflakes = json.loads(f.read())

    # Transform from base64 to hex32 lexicographically sortable.
    hex_elasticflakes = list(
        map(
            lambda x: (x[1], base64.b32hexencode(base64.urlsafe_b64decode(x[0])).decode()),
            elasticflakes
        )
    )

print('Before shuffling')
print('is sorted elasticflakes:', is_sorted(elasticflakes, 1))
print('is sorted hex_elasticflakes:', is_sorted(hex_elasticflakes, 0))

random.shuffle(elasticflakes)
random.shuffle(hex_elasticflakes)

print('After shuffling')
print('is sorted elasticflakes:', is_sorted(elasticflakes, 1))
print('is sorted hex_elasticflakes:', is_sorted(hex_elasticflakes, 0))


elasticflakes.sort(key=lambda x: x[0])
hex_elasticflakes.sort(key=lambda x: x[1])

print('after sorting')
print('is sorted elasticflakes:', is_sorted(elasticflakes, 1))
print('is sorted hex_elasticflakes:', is_sorted(hex_elasticflakes, 0))
