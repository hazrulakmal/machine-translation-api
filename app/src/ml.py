
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from pathlib import Path

class TranslationModel:
    def __init__(self, model_chckpt:str, from_hub:bool=False):
        if from_hub:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_chckpt)
            self.tokenizer = AutoTokenizer.from_pretrained(model_chckpt, return_tensors="pt")
        else:
            base_dir = Path(__file__).resolve(strict=True).parent.parent
            self.model = AutoModelForSeq2SeqLM.from_pretrained(Path(f"{base_dir}/models/{model_chckpt}")) #(f"../models/{model_chckpt}")
            self.tokenizer = AutoTokenizer.from_pretrained(Path(f"{base_dir}/tokenizers/{model_chckpt}")) #(f"../tokenizers/{model_chckpt}")
            
    def predict(self, inputs:str):
        """
        Predicts the translation of the input text using the model and tokenizer
        :param inputs: The input text to be translated
        :return: The translated text
        """		
        predictions = self.model.generate(self.tokenizer(inputs, return_tensors="pt").input_ids)
        predictions = predictions.cpu().numpy()
        decoded_preds = self.tokenizer.decode(predictions[0], skip_special_tokens=True)
        return decoded_preds
    
    def save(self, model_path:str, tokenizer_path:str):
        """
        Saves the model and tokenizer to the specified path
        :param path: The path to save the model and tokenizer
        """
        self.model.save_pretrained(model_path)
        self.tokenizer.save_pretrained(tokenizer_path)

#model = TranslationModel("opus-mt-en-id")


