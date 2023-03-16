# machine-translation-api
Deploying machine learning models using Bentoml via RESTful API

## Installation
1. Clone the repository
2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```
3. install dependencies from requirements.txt
```bash 
pip install -r requirements.txt
```

## Usage
1. Fetch model from huggingface hub and save it as a bentoml model
```bash
python src/save_model.py
```
2. Star the bentoml developement server
```bash
bentoml serve service:svc 
```
3. Open http://127.0.0.1:3000 in your browser and send test request from the web UI.
Make sure to specify three important components in the request body. For example:
```json
{
    "text": "Hello world",
    "source_language": "en",
    "target_language": "id"
}
```


To-list

1. register free gsc
2. save model using bentoml to gsc bucket (save the pipeline)
3. copy code from transform example
4. deploy using yatai (kubernetes) throus aws lambda
5. build a gradio ui on a seperate file deploy in on huggingface spaces