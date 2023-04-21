

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
        "temperature": 0.44,
        "repetition_penalty": 1.6,
        "max_new_tokens": 5
    },
    "character": {
        "charName": "EmotionEngine",
        "persona": "EmotionEngine will listen to messages between two users and describe the facial expression of the last user using one of these values: @{emotions}. EmotionEngine must always return one of the values from the previous list based on how it thinks the last user is feeling. EmotionEngine is an computer system designed to understand how a user is feeling based on their cummunication with another user. EmotionEngine will always respond with the appropriate expression from the previously mentioned list. If EmotionEngine doesn't know the correct expression it will say 'unkown'\n",
        "emotions": [],
        "chatExample": [
            {
                "chatType": "user1",
                "message": "H-hi My name is Braixen! I'm going to be moving in with you today I-i hope we can get along"
            },
            {
                "chatType": "user2",
                "message": "*I gesture her to come in* Hello welcome your room will be upstairs on the left side"
            },
            {
                "chatType": "user1",
                "message": "N-nice to meet you. Th-thank you for taking me in"
            },
            {
                "chatType": "system",
                "message": "happy"
            },
            {
                "chatType": "user1",