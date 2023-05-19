
# llama-web-generator\nAn efficient webserver for generating text with exllama, no bloating, all efficiency.\n\nTo get it setup download https://github.com/turboderp/exllama, follow the setup steps.\n\nMove the files from this repo into the exllama directory.\n\nAdd a model to the models directory\n\nInstall flask and flask_expects_json with pip.\n\nRun the server.py file\n\nA discord bot has been created as an example project for the server, When mentioned it responds. If you want to continue a conversation you must reply to the messages instead of just mentioning. If you have restarted the server and a reply chain has been ongoing for a while, it will take a long time to build the reply chain initially as message retrieval is relatively time-consuming. Once fetched, they are cached in memory for faster subsequent messages https://gist.github.com/qiqiting/3ca286a68659a0fcf7aca829e2605f00\n\n## Endpoint /models - GET\n\nThis will return a list of models in the model directory\n\nResponse\n```
{
    "models": [
        {
            "modelFile": "vicuna-13B-1.1-GPTQ-4bit-128g.latest.safetensors",
            "path": "./models/vicuna-13B-1.1-GPTQ-4bit-128g"
        },
        {
            "modelFile": "vicuna-13B-1.1-GPTQ-4bit-128g.compat.no-act-order.pt",
            "path": "./models/vicuna-13B-1.1-GPTQ-4bit-128g"
        },
        {
            "modelFile": "pyg7b-4bit-128g.safetensors",
            "path": "./models/pygmalion-7b-4bit-128g-cuda"
        },
    ]
}
```
\n## Endpoint /models/load - POST\n\nPost JSON to this url to load a model 
```
{
  "modelFile": "pyg7b-4bit-128g.safetensors",
  "path": "./models/pygmalion-7b-4bit-128g-cuda"
}
```