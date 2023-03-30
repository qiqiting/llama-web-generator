
chatSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "userName": {
            "type": "string"
        },
        "genParams": {
            "type": "object",
            "properties": {
                "min_length": {
                    "type": "integer"
                },
                "max_length": {
                    "type": "integer"
                },
                "top_p": {
                    "type": "number"
                },
                "min_p": {
                    "type": "number"
                },
                "top_k": {
                    "type": "number"
                },
                "temperature": {
                    "type": "number"
                },
                "token_repetition_penalty_max": {
                    "type": "number"
                },
                "token_repetition_penalty_sustain": {
                    "type": "integer"
                },