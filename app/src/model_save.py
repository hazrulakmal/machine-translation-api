from ml import TranslationModel
from pathlib import Path

checkpoint = "Helsinki-NLP/opus-mt-en-id"
model_path = Path("../models/")
tokenizer_path = Path("../tokenizers/")

if __name__ == '__main__':
    model = TranslationModel(checkpoint, from_hub=True)
    name = checkpoint.split("/")[-1]
    model.save(model_path.joinpath(name), tokenizer_path.joinpath(name))