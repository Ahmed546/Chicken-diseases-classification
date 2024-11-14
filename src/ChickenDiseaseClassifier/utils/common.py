import os
from box.exceptions import BoxValueError
import yaml
from ChickenDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
# from box import Box, BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """Read yaml file and return
    Args:
        path_to_yaml (str): Path like input

    Raises:
        valueError: If yaml file is not valid 
        e:empty dictionary
    
    Returns:
        ConfigBox: ConfigBox object

    """
    try:
        with open(path_to_yaml, 'r') as file:
            config_data = yaml.safe_load(file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
        if not config_data:
            raise BoxValueError("Empty dictionary")
        return ConfigBox(config_data)
    except BoxValueError:
        logger.error(f"File not found: {path_to_yaml}")
        raise ValueError(f"File not found: {path_to_yaml}")
    except Exception as e:
        logger.error(f"Invalid YAML file: {path_to_yaml}")
        raise e

# @ensure_annotations
# def read_yaml(path_to_yaml: Path) -> Box:
#     """Read YAML file and return its content as a Box object.

#     Args:
#         path_to_yaml (Path): Path to the YAML file.

#     Raises:
#         ValueError: If the YAML file is empty or not found.
#         Exception: For other YAML-related errors.

#     Returns:
#         Box: Box object containing the YAML file data.
#     """
#     try:
#         with open(path_to_yaml, 'r') as file:
#             config_data = yaml.safe_load(file)
#             logger.info(f"Successfully loaded YAML file: {path_to_yaml}")

#         if not config_data:
#             raise BoxValueError("Empty dictionary")

#         return Box(config_data)

#     except FileNotFoundError:
#         logger.error(f"File not found: {path_to_yaml}")
#         raise ValueError(f"File not found: {path_to_yaml}")

#     except BoxValueError:
#         logger.error(f"YAML file is empty: {path_to_yaml}")
#         raise ValueError("YAML file is empty")

#     except yaml.YAMLError as e:
#         logger.error(f"Invalid YAML file: {path_to_yaml}")
#         raise ValueError(f"Invalid YAML file: {e}")
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories
    Args:
        path_to_directories(list): list of path of directories
        ingore_log(bool,optional):ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """Save dictionary to json file
    Args:
        path (Path): Path like output
        data (dict): dictionary to save
    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        logger.info(f"Successfully saved JSON file: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"