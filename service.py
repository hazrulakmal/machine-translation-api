import bentoml
from bentoml.io import JSON, Text
from pydantic import BaseModel

class inputText(BaseModel):
    text: str
    source_language: str
    target_language: str

# Load the BentoML bundle
translation_en_id = bentoml.transformers.get("en_id:latest").to_runner()
translation_id_en = bentoml.transformers.get("id_en:latest").to_runner()
model_available ={
    "en_id": translation_en_id,
    "id_en": translation_id_en,
}

svc = bentoml.Service(
    "multi-translator",
    runners=[
        translation_en_id,
        translation_id_en,
    ],
)

@svc.api(input=JSON(pydantic_model=inputText), output=Text())
async def translate(inputdata: inputText) -> str:
    source, target = inputdata.source_language, inputdata.target_language
    input_sentence = inputdata.text
    if f"{source}_{target}" in model_available:
        model = model_available[f"{source}_{target}"]
        tranlated_sentence = await model.async_run(input_sentence)
        return tranlated_sentence[0]["translation_text"]
    else:
        return "Translation not available"
 