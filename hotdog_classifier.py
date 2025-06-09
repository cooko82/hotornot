import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("hotdog_model.h5")

def classify(img):
    img = img.resize((224, 224))  # Ensure it's PIL, then resize
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)[0][0]
    label = "Hot Dog! 🌭" if prediction < 0.5 else "Not Hot Dog - You should have gone to specsavers silly Billy ❌"
    #return f"{label} ({prediction:.2f})"
    return f"{label}"

#gr.Interface(fn=classify, inputs=gr.Image(type="pil"), outputs="text").launch()

with gr.Blocks() as demo:
    gr.Markdown("# 🌭 Hotdog or Not Hotdog Classifier")
    gr.Markdown("Upload a photo and find out whether it's a hotdog or... **not**.")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload your food photo 🍽️")
        label_output = gr.Textbox(label="Result")

    submit_btn = gr.Button("🔥 Classify")
    submit_btn.click(fn=classify, inputs=image_input, outputs=label_output)

    gr.Markdown("---")
    gr.Markdown("Techstack: TensorFlow + Gradio")

demo.launch()