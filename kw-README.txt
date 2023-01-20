Dir structure:

NAISC
|   README.txt
|   
+---env  # Virtual env
|
\---human_detection  # A PeekingDuck project. Might create more idk
    |   pipeline_config.yml
    |   
    +---data  # Inputs for our project
    |       hawker01.png
    |       hawker_video.mp4
    |       
    +---output # Output directory
    |       hawker01_230119_234230.png
    |               
    \---src  # More advanced stuff will go here. Still figuring it out
        \---custom_nodes
            \---configs


Usage guide:


cd to NAISC folder (it will act as the home directory)


run the following line to activate virtual env:
env\Scripts\activate

(i think?) for macOS run:
source pkd/bin/activate


To run a specific peekingduck project, cd into the project folder (e.g. cd human_detection)
Then do `peekingduck run`
To set up a new project, create a new folder with the project name. cd into it and do `peekingduck init`.
To edit a project in the basic ways, edit the pipeline_config.yml file.


Examples:  # So far yolo seems to be the best model


# The following config will save the processed file (pic or vid) to the default dir (which is ~/proj_name/PeekingDuck/data/output)
nodes:
- input.visual:
    source: data/hawker01.png
- model.yolo:
    detect: ["person"]
- draw.bbox:
    show_labels: True
- output.media_writer


# The following will display the processed video 
nodes:
- input.visual:
    source: data/hawker_video.mp4
- model.yolo:
    detect: ["person", "cup", "dining table", "chair"]
- draw.bbox:
    show_labels: True
- output.screen
