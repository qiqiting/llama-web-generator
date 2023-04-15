

from copy import deepcopy
import json
from flask import Flask, g, request
import torch
from repos.model_repo import LlamaModel, LlamaModelRepo
from flask_expects_json import expects_json
import schema
app = Flask(__name__)

modelRepo = LlamaModelRepo()
llamaModel = None
model = None


emotionsPromptTemplate = {
    "firstUser": "User1",
    "secondUser": "User2",
    "genParams": {
        "max_length": 1000,
        "top_p": 0.7,