"""
Video Settings
"""
RESOLUTION = [1920, 1080]
FPS = 15  # Reduce FPS to reduce live stream lag

"""
Zone Settings
zone is a list of bounding boxes
Each bounding box is a list of four [x,y] coords, corresponding to the 4 corners of box
May use relative coords (between 0 and 1) or absolute coords
If using relative coords, need to specify the resolution of input
"""
ALL_IN_ONE = [[[0, 0], [0, 1], [1, 1], [1, 0]]]
VERTICAL_SPLIT = [
    [[0, 0], [0.5, 0], [0.5, 1], [0, 1]],
    [[0.5, 0], [1, 0], [1, 1], [0.5, 1]]]

CAMERA_A_ZONES = [[[701, 483], [1086, 483], [1086, 867], [701, 867]], [[1217, 531], [1891, 531], [1891, 867], [1217, 867]], [[768, 322], [1045, 322], [1045, 469], [768, 469]], [[1166, 324], [1666, 324], [1666, 567], [1166, 567]], [[838, 41], [1000, 41], [1000, 234], [838, 234]], [[1078, 63], [1397, 63], [1397, 322], [1078, 322]], [[549, 111], [822, 111], [822, 477], [549, 477]]]
CAMERA_A_MAPPING = [100, 101, 102, 103, 104, 105, 0]

CAMERA_B_ZONES = [[[10, 537], [602, 537], [602, 936], [10, 936]], [[783, 551], [1092, 551], [1092, 889], [783, 889]], [[254, 412], [703, 412], [703, 680], [254, 680]], [[821, 416], [1076, 416], [1076, 596], [821, 596]], [[527, 193], [780, 193], [780, 430], [527, 430]], [[897, 139], [1022, 139], [1022, 430], [897, 430]]]
CAMERA_B_MAPPING = [106, 107, 108, 109, 110, 111]

CAMERA_C_ZONES = [[[553, 830], [1358, 830], [1358, 1078], [553, 1078]], [[223, 713], [610, 713], [610, 1018], [223, 1018]], [[801, 352], [990, 352], [990, 516], [801, 516]], [[76, 529], [1137, 529], [1137, 871], [76, 871]]]
CAMERA_C_MAPPING = [120, 121, 122, 1]

CAMERA_D_ZONES =[[[867, 928], [1412, 928], [1412, 1076], [867, 1076]], [[1477, 924], [1911, 924], [1911, 1075], [1477, 1075]], [[832, 717], [1178, 717], [1178, 944], [832, 944]], [[1260, 717], [1665, 717], [1665, 965], [1260, 965]], [[781, 400], [1153, 400], [1153, 682], [781, 682]], [[1180, 559], [1565, 559], [1565, 752], [1180, 752]]]
CAMERA_D_MAPPING = [130, 131, 132, 133, 134, 2]

CAMERA_E_ZONES = [[[527, 889], [1194, 889], [1194, 1076], [527, 1076]], [[1428, 834], [1866, 834], [1866, 1078], [1428, 1078]], [[828, 611], [1225, 611], [1225, 912], [828, 912]], [[1330, 613], [1790, 613], [1790, 873], [1330, 873]], [[703, 438], [1012, 438], [1012, 649], [703, 649]], [[1047, 414], [1405, 414], [1405, 610], [1047, 610]]]
CAMERA_E_MAPPING = [140, 141, 142, 143, 144, 145]

CAMERA_IDS = {"CAMERA_A", "CAMERA_B", "CAMERA_C", "CAMERA_D", "CAMERA_E"}
ZONES = {"CAMERA_A": CAMERA_A_ZONES, "CAMERA_B": CAMERA_B_ZONES, "CAMERA_C": CAMERA_C_ZONES, "CAMERA_D": CAMERA_D_ZONES, "CAMERA_E": CAMERA_E_ZONES}
MAPPINGS = {"CAMERA_A": CAMERA_A_MAPPING, "CAMERA_B": CAMERA_B_MAPPING, "CAMERA_C": CAMERA_C_MAPPING, "CAMERA_D": CAMERA_D_MAPPING, "CAMERA_E": CAMERA_E_MAPPING}
INPUT_PATHS = {"CAMERA_A": "data/A.mp4", "CAMERA_B": "data/B.mp4", "CAMERA_C": "data/C.mp4", "CAMERA_D": "data/D.mp4", "CAMERA_E": "data/E.mp4"}
