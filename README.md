# Hawk-Eye Centre AI Repository

## Directory Structure
```
project
│   README.md # readme file
│   kw-README.txt # original readme from kw
│   .gitignore # gitignore file
|   pkd-macos-silicon.yml # yml file for conda environment in apple silicon
|   requirements.txt # venv file for non apple silicon
|
└───human_detection
    │   pipeline_config.yml # Config file for peekingduck project
    │
    └───data # Inputs for our project
    │   │   hawker01.png
    │   │   hawker02.png
    │   │   ...
    │
    └───output # Output directory
    │   │   hawker05_230120_152839.png
    │   │   ...
    │
    └───src # To add custom nodes
        │
        └custom_nodes
            │
            └config

```

## To Install

### For Windows

```sh
python -m venv pkd
pkd\Scripts\activate
pip install -r requirements.txt
```

### For MacOS Apple Silicon

```sh
conda env create -f pkd-macos-silicon.yml
conda activate pkd
```

### For MacOS Intel & Linux

```sh
conda create -n pkd python=3.8
conda activate pkd
pip install -r requirements.txt
```

## To Run

1. To run a specific peekingduck project, cd into the project folder (e.g. cd human_detection)
2. Do `peekingduck run`

## To Setup a new project

1. To set up a new project, create a new folder with the project name. cd into it and do `peekingduck init`.
2. To edit a project in the basic ways, edit the pipeline_config.yml file.


## Examples for pipeline_config.yml

The following config will save the processed file (pic or vid) to the default dir (which is `~/proj_name/PeekingDuck/data/output`)
```
nodes:
- input.visual:
    source: data/hawker01.png
- model.yolo:
    detect: ["person"]
- draw.bbox:
    show_labels: True
- output.media_writer:
    output_dir: output
```

The following will display the processed video 
```
nodes:
- input.visual:
    source: data/hawker_video.mp4
- model.yolo:
    detect: ["person", "cup", "dining table", "chair"]
- draw.bbox:
    show_labels: True
- output.screen
```

