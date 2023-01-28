from pathlib import Path
import cv2
from settings_golden_mile import *

from peekingduck.pipeline.nodes.dabble import fps, zone_count, bbox_count, bbox_to_btm_midpoint
from peekingduck.pipeline.nodes.draw import bbox, legend, zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner

def is_table_occupied(record):
    result = []
    for zone_id in range(len(record[0])):
        # Cumulative avg >= 0.75 to filter out noise e.g. people passing by
        result.append(sum([row[zone_id] for row in record])/len(record) >= 0.75)
    return result



def count_human_gen(path_to_file):
    # input
    visual_node = visual.Node(source=path_to_file, buffering=True)

    # Model
    # yolo_node = yolo.Node(detect=["person", "cup", "dining table", "chair", "fork", "knife", "spoon", "bowl", "banana", "wine glass", "bird"])
    yolo_node = yolo.Node(detect=["person"])

    # Dabble
    bbox_count_node = bbox_count.Node()
    bbox_to_btm_midpoint_node = bbox_to_btm_midpoint.Node()  # Convert to btm_midpoint to feed into zone_count_node
    zone_count_node = zone_count.Node(zones=ZONE_B, resolution=RESOLUTION)

    # Draw
    bbox_node = bbox.Node(show_labels=True)
    zones_node = zones.Node()
    legend_node = legend.Node(show=["bbox_count","zone_count"])

    # Output
    media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "output"))

    # Manually run the pipeline
    zone_count_records = []
    while True:
        visual_output = visual_node.run({})
        if visual_output["pipeline_end"]: break  # Video has no more frames

        yolo_output = yolo_node.run({"img":visual_output["img"]})
        bbox_count_output = bbox_count_node.run({"bboxes": yolo_output["bboxes"]})
        bbox_to_btm_midpoint_output = bbox_to_btm_midpoint_node.run({"img": visual_output["img"], "bboxes": yolo_output["bboxes"]})
        zone_count_output = zone_count_node.run({"btm_midpoint": bbox_to_btm_midpoint_output["btm_midpoint"]})

        bbox_node.run({"img": visual_output["img"],
                       "bboxes": yolo_output["bboxes"],
                       "bbox_labels": yolo_output["bbox_labels"]})
        zones_node.run({"img": visual_output["img"],
                        "zones": zone_count_output["zones"]})
        legend_output = legend_node.run({"img": visual_output["img"],
                                         "bbox_count": bbox_count_output["count"],
                                         "zone_count":zone_count_output["zone_count"]})
        media_writer_node.run({"img":legend_output["img"],
                               "filename":visual_output["filename"],
                               "saved_video_fps":visual_output["saved_video_fps"],
                               "pipeline_end":visual_output["pipeline_end"]})

        if len(zone_count_records) > visual_output["saved_video_fps"]*3:  # Records last 3s
            zone_count_records.pop(0)
        zone_count_records.append(zone_count_output["zone_count"])
        table_occupation = is_table_occupied(zone_count_records)
        # zone_count indicates the number of bboxes with bottom midpoint lying in the zone boundary
        yield {"img": legend_output["img"],
               "total_count": bbox_count_output["count"],
               "table_count": zone_count_output["zone_count"],
               "table_occupation": table_occupation,
               "occupied_table_count": sum(table_occupation),
               "empty_table_count": table_occupation.count(False)}


generator = count_human_gen(str(Path.cwd() / "data" / "Golden Mile" / "B.mp4"))
while True:
    try:
        res = next(generator)
        print(res["total_count"])
        print(res["table_count"], res["table_occupation"], res["occupied_table_count"])
        # cv2.imshow("img", res["img"])
        # cv2.waitKey(0)
        # break
    except:
        print("End of Video")
        break