from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps, zone_count, bbox_count, bbox_to_btm_midpoint
from peekingduck.pipeline.nodes.draw import bbox, legend, zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner


def main():
    # input
    visual_node = visual.Node(source=str(Path.cwd() / "data" / "queue01.mp4"))

    # Model
    # yolo_node = yolo.Node(detect=["person", "cup", "dining table", "chair", "fork", "knife", "spoon", "bowl", "banana", "wine glass", "bird"])
    yolo_node = yolo.Node(detect=["person"])

    # Dabble
    # bbox_count_node = bbox_count.Node()
    bbox_to_btm_midpoint_node = bbox_to_btm_midpoint.Node()  # Convert to btm_midpoint to feed into zone_count_node
    """
    zones is a list of bounding boxes
    Each bounding box is a list of four [x,y] coords, corresponding to the 4 corners of box
    May use relative coords (between 0 and 1) or absolute coords
    If using relative coords, need to specify the resolution of input
    """
    all_in_one = [[[0,0],[0,1],[1,1],[1,0]]]
    single_cropped = [[[0.3, 0.2], [0.7, 0.2], [0.7, 0.8], [0.3, 0.8]]]
    vertical_split = [
        [[0,0],[0.5,0],[0.5,1],[0,1]],
        [[0.5,0],[1,0],[1,1],[0.5,1]]
    ]
    zone_count_node = zone_count.Node(zones=single_cropped, resolution = [1920,1080])

    # Draw
    bbox_node = bbox.Node(show_labels=True)
    zones_node = zones.Node()
    legend_node = legend.Node(show=["zone_count"])

    # Output
    screen_node = screen.Node()
    media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "output"))

    # Compile the nodes and run
    runner = Runner(
        nodes=[
            visual_node,
            yolo_node,
            # bbox_count_node,
            bbox_to_btm_midpoint_node,
            zone_count_node,
            legend_node,
            bbox_node,
            zones_node,
            screen_node,
            media_writer_node,
        ]
    )
    runner.run()


if __name__ == "__main__":
    main()