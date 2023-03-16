#from ml import TranslationModel
import bentoml
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

checkpoint_en_id = "Helsinki-NLP/opus-mt-en-id"
checkpoint_id_en = "Helsinki-NLP/opus-mt-id-en"

if __name__ == '__main__':
    # Load the model
    translation_en_id = pipeline(
        task="translation",
        model=AutoModelForSeq2SeqLM.from_pretrained(checkpoint_en_id),
        tokenizer=AutoTokenizer.from_pretrained(checkpoint_en_id),
    )

    translation_id_en = pipeline(
        task="translation",
        model=AutoModelForSeq2SeqLM.from_pretrained(checkpoint_id_en),
        tokenizer=AutoTokenizer.from_pretrained(checkpoint_id_en),
    )

    # Save the model
    m1 = bentoml.transformers.save_model("en_id", 
                                         translation_en_id,
                                         labels={"pair": "en_id", "version": "v1"})
    m2 = bentoml.transformers.save_model("id_en", 
                                         translation_id_en,
                                         labels={"pair": "id_en", "version": "v1"})

    print(f"Model Saved: {m1}, {m2}")
