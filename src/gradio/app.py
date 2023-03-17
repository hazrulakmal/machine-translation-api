import gradio as gr
import requests

PREDICTION_ENDPOINT = "http://localhost:3000/translate" # Change this to your endpoint

# Define a custom validation function that checks if the input fields are filled
def validate_inputs(text, source_lang, target_lang):
    if text and source_lang and target_lang:
        return True, None
    else:
        return False, "Please fill up all input fields"
    
# Define the translation function
def translate_text(text, source_language, target_language):
    #text, source_language, target_language = inputs["text"], inputs["source_language"], inputs["target_language"]
    validation, message = validate_inputs(text, source_language, target_language)
    if validation:
        responds = requests.post(PREDICTION_ENDPOINT, 
                             json={"text": text, 
                                    "source_language": source_language,
                                    "target_language": target_language}
        )
        return responds.text
    else:
        return message

# Define the Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        input_text = gr.Textbox(label="Enter text to translate")
    with gr.Row():    
        source = gr.Dropdown(["en", "id"], label="Source Language",  value="en")
        target = gr.Dropdown(["en", "id"], label="Target Language",  value="id")
    with gr.Row():
        output = gr.Textbox(label="Translated text")
    with gr.Row():
        sumbit_btn = gr.Button("submit")
        #input_dict = {"text": input_text, "source_language": source, "target_language": target}
        sumbit_btn.click(translate_text, inputs=[input_text, source, target], outputs=output)

# Launch the Gradio web UI in development mode
demo.launch()


        