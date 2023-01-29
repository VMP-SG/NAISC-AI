from table_count_generator import *
from settings_golden_mile import *

"""
API sample output
{
    "CAMERA_A": {
        "raw_frame": [..img..],
        "labelled_frame": [..img..],
        "total_people_count": 10,
        "zone_people_count": [2, 2, 0, 0],
        "mapping": [1, 3, 2, 5]
    },
    "CAMERA_B": {
        ...
    }
}
"""


def run_API():
    generators = {camera_id:count_human_gen(INPUT_PATHS[camera_id], ZONES[camera_id], RESOLUTION, MAPPINGS[camera_id]) for camera_id in CAMERA_IDS}
    yield {camera_id:next(generators[camera_id]) for camera_id in CAMERA_IDS}

# API = run_API()
# print(next(API))