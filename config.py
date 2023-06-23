import os
from mazelib.algorithms import *

# ======================================================================================================================
#       Maze Settings
# ======================================================================================================================

ALLOWED_ALGORITHMS = [
    BinaryTree,
    AldousBroder,
    Prims,
    BacktrackingGenerator
]

NUMBER_OF_MAZES = 100000
TRAINING_PERCENT = 0.9

MIN_HEIGHT = 5
MAX_HEIGHT = 5
MIN_WIDTH = 5
MAX_WIDTH = 5

# ======================================================================================================================
#       Tokenizer
# ======================================================================================================================

PAD_TOKEN = "[PAD]"
MASK_TOKEN = "[MASK]"

SPECIAL_TOKENS = [
    PAD_TOKEN,
    MASK_TOKEN
]

# ======================================================================================================================
#       Folder / File Names
# ======================================================================================================================

OUTPUT_DIRECTORY_NAME = "out"
MODEL_DIRECTORY_NAME = "model"
DATA_DIRECTORY_NAME = "data"

DATA_FILENAME = "dataset.txt"
TOKENIZER_FILENAME = "tokenizer.json"
SELECTED_MODEL = "checkpoint-3510"

# ======================================================================================================================
#       Paths
# ======================================================================================================================

ROOT_PATH = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(ROOT_PATH, OUTPUT_DIRECTORY_NAME)

MODEL_DIRECTORY = os.path.join(OUTPUT_PATH, MODEL_DIRECTORY_NAME)
MODEL_PATH = os.path.join(MODEL_DIRECTORY, SELECTED_MODEL)

DATA_DIRECTORY = os.path.join(OUTPUT_PATH, DATA_DIRECTORY_NAME)
DATA_FILE_PATH = os.path.join(DATA_DIRECTORY, DATA_FILENAME)
TOKENIZER_FILE_PATH = os.path.join(OUTPUT_DIRECTORY_NAME, TOKENIZER_FILENAME)