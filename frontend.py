import streamlit as st
import torch
from transformers import ViTForImageClassification, ViTFeatureExtractor
from PIL import Image

model_name = './vit-beans'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def run_model(image):    

    model = ViTForImageClassification.from_pretrained(model_name)
    model.eval()
    model.to(device)

    feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
    encoding = feature_extractor(image, return_tensors='pt')
    pixel_values = encoding['pixel_values'].to(device)

    output = model(pixel_values)
    logits = output.logits

    pred = logits.argmax(-1)
    return model.config.id2label[pred.item()]
    
st.write("""
# Leaf Anomaly Detector
This will detect anomalies on the leaf and output if the leaf is healthy or not.
""")

image = st.file_uploader('Choose a leaf picture to upload')

if image is not None:

    image_load_state = st.text('Loading data...')
    image = Image.open(image)
    st.image(image , caption='Your Image')
    
    image_load_state.text('Running model...')
    pred = run_model(image)
    image_load_state.text('Output')
    if pred == 'healthy':
        st.subheader('Your leaf looks: ' + pred)
    else: 
        st.subheader('Your leaf doesnt look very good, it has - ' + pred)