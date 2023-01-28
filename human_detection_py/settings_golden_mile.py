"""
Video Settings
"""
RESOLUTION = [1920, 1080]


"""
Zone Settings
zones is a list of bounding boxes
Each bounding box is a list of four [x,y] coords, corresponding to the 4 corners of box
May use relative coords (between 0 and 1) or absolute coords
If using relative coords, need to specify the resolution of input
"""
ALL_IN_ONE = [[[0, 0], [0, 1], [1, 1], [1, 0]]]
VERTICAL_SPLIT = [
    [[0, 0], [0.5, 0], [0.5, 1], [0, 1]],
    [[0.5, 0], [1, 0], [1, 1], [0.5, 1]]
]
ZONE_B = [
    [[0, 0.45],[0, 0.8],[0.3, 0.8],[0.3, 0.45]],
    [[0.41, 0.45],[0.41, 0.8],[0.6, 0.8],[0.6, 0.45]],
]