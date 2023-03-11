
from enum import Enum
from genericpath import exists
import os
import re

import torch
from model import ExLlama, ExLlamaCache, ExLlamaConfig
from tokenizer import ExLlamaTokenizer
from generator import ExLlamaGenerator

# Used in json if &{key} exists in a value it should be replaced with a value from the main json dict such as userName
mainDictTarget = "&"
# Used in json if @{key} exists in a value it should be replaced with a value from the character json dict such as charName
characterDictTarget = "@"


class ModelType(Enum):
    SAFETENSORS = "safetensors"
    PT = "pt"


class LlamaModel(dict):
    path = str
    modelFile = str