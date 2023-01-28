from pathlib import Path
import cv2

from peekingduck.pipeline.nodes.dabble import fps, zone_count, bbox_count, bbox_to_btm_midpoint
from peekingduck.pipeline.nodes.draw import bbox, legend, zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner


def count_human(frame, video_name=""):
    # input
    yolo_input = {"img": frame}

    # Model
    yolo_node = yolo.Node(detect=["person"])

    # Dabble
    bbox_count_node = bbox_count.Node()

    # Draw
    bbox_node = bbox.Node(show_labels=True)
    legend_node = legend.Node(show=["bbox_count"])

    # Output
    screen_node = screen.Node()
    if video_name:
        media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "output" / video_name))
    else:
        media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "output"))

    # Manually run the pipeline
    yolo_output = yolo_node.run({"img":yolo_input["img"]})
    bbox_count_output = bbox_count_node.run({"bboxes":yolo_output["bboxes"]})
    # return bbox_count_output["count"]

    # The following nodes has no outputs
    bbox_node.run({"img":yolo_input["img"], "bboxes":yolo_output["bboxes"], "bbox_labels":yolo_output["bbox_labels"]})
    legend_output = legend_node.run({"img":yolo_input["img"], "bbox_count":bbox_count_output["count"]})

    # screen_node.run({"img":legend_output["img"], "filename":yolo_input["filename"]})
    media_writer_node.run({"img":legend_output["img"],
                           "filename": video_name + "frame.png",
                           "saved_video_fps":10,
                           "pipeline_end":False})
    return bbox_count_output["count"]


def count_human_gen(filename):  # Input should be a video file name, stored in the data folder
    video = cv2.VideoCapture(str(Path.cwd() / "data" / filename))
    if video.isOpened() == False:
        print("Error opening video")

    while video.isOpened():
        ret, frame = video.read()
        if ret:
            yield count_human(frame, filename)
        else:
            break
    video.release()

generator = count_human_gen("golden_mile01.mp4")
for _ in range(10):
    print(next(generator))