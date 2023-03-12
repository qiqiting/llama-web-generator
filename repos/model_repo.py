
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
    ModelType = ModelType

    def __init__(self, path: str, modelFile: str):
        dict.__init__(self, path=path, modelFile=modelFile)
        self.path = path
        self.modelFile = modelFile
        self.modelType = ModelType(modelFile[modelFile.rfind(".") + 1:])


class LlamaModelRepo:
    tokenizer: ExLlamaTokenizer = None
    generator: ExLlamaGenerator = None
    config: ExLlamaConfig = None
    model: ExLlama = None
    cache: ExLlamaCache = None

    def __init__(self):
        self.models: list = []
        self.modelsDir: str = './models'

    def getModelsFromSubDir(self, path: str):
        models: list = []
        for filename in os.listdir(path):
            print(filename)
            if filename[filename.rfind(".") + 1:] in [e.value for e in ModelType]:

                models.append(LlamaModel(path, filename))
                print(path, flush=True)
        return models