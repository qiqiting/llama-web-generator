
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