from fastapi import FastAPI
from pydantic import BaseModel
from ml import TranslationModel

app = FastAPI()

class TextIn(BaseModel):
    sentence: str
    model: str

class TextOut(BaseModel):
    sentence: str

@app.get("/")
def home():
    return {"Health_check": "Ok"}

@app.post("/translate", response_model=TextOut)
def translate(inputs: TextIn):
    model = TranslationModel(inputs.model)
    tranlsated_sentence = model.predict(inputs.sentence)
    return {"sentence": tranlsated_sentence}

