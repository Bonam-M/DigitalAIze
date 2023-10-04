import os
import io
import tempfile
import streamlit as st
import requests
from PIL import Image
import fitz #PyMuPDF
import base64
import configparser
import config

# Function to read API key from the configuration file
#def get_api_key():
    #config = configparser.ConfigParser()
    #config.read('config.ini')  # Adjust the path if the config file is located elsewhere
    #return config['GoogleCloud']['api_key']

# Set your Google Cloud API key
api_key = st.secrets.googlecloud_credentials.api_key 

# Function to call Google Cloud Vision API for text detection
def detect_text(image_base64):
    endpoint = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key
    headers = {"Content-Type": "application/json"}
    data = {
        "requests": [
            {
                "image": {"content": image_base64},
                "features": [{"type": "DOCUMENT_TEXT_DETECTION"}],
            }
        ]
    }
    response = requests.post(endpoint, headers=headers, json=data)
    return response.json()

# Function to process PDF file into images using PyMuPDF
def process_pdf(pdf_file):
    images_and_texts = []  # Store extracted text and images
    pdf_document = fitz.open(pdf_file)
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_bytes = page.get_pixmap().tobytes()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')  # Encode as base64
        response = detect_text(image_base64)  # Image data is in base64

        if "error" in response:
            st.error(f"Error on Page {page_num + 1}: {response['error']['message']}")
        else:
            text_annotations = response['responses'][0].get('fullTextAnnotation', {})
            extracted_text = text_annotations.get('text', '')
            images_and_texts.append((image_bytes, extracted_text))

    return images_and_texts

# Streamlit UI
st.set_page_config(
    page_title="Handwritten To text",
    page_icon="📄",
)

st.title("📄 Handritten to Text (HTT) ")

st.markdown(
    """
    **HTT** is a Machine Learning solution
    that convert pictures of handwritten documents into text files.    
"""
)
multi = '''
**👇 Follow the instructions below** to convert your files.  
    Use these files for a quick demo  
    - A PNG file of a [one handwritten note](https://drive.google.com/file/d/1L1rlkCFEH-oug-W9NZwUhQShqQFlqcq9/view?usp=sharing)  
    - A three pages long PDF file of [three handwritten notes](https://drive.google.com/file/d/1PWNXq5RzCZB35hjjcYx5Jsv4Whcgr_n1/view?usp=sharing)  
    - A seven pages long PDF file of [multilingual handwritten notes](https://drive.google.com/file/d/1KxDEloBOtFwKA4pLRo7E8P_0mwJzU0T3/view?usp=sharing)  
    or use your own files and try it out!  
      

'''
st.markdown(multi)

file_upload = st.file_uploader("Upload a picture of a handwritten document or a PDF file", type=["jpg", "jpeg", "png", "pdf"])

if file_upload is not None:
    with st.spinner("Processing..."):
        if file_upload.type == "application/pdf":
            pdf_path = os.path.join(tempfile.gettempdir(), "temp.pdf")
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(file_upload.read())

            images_and_texts = process_pdf(pdf_path)

            # Display images and extracted text
            for i, (image_bytes, extracted_text) in enumerate(images_and_texts):
                st.image(Image.open(io.BytesIO(image_bytes)), caption=f"Page {i + 1}", use_column_width=True)
                st.subheader(f"Extracted Text (Page {i + 1}):")
                st.write(extracted_text)

            # Create a combined text for download
            combined_text = "\n\n".join([f"Page {i + 1}:\n{extracted_text}" for i, (_, extracted_text) in enumerate(images_and_texts)])
            st.subheader("Extracted Text from Document:")
            st.write(combined_text)

            # Add download button for all pages as a single text file
            st.download_button(
                label="Download Text File",
                data=combined_text,
                key="download_all",
                on_click=None,
                args=("extracted_text_all.txt",),
            )
        else:
            # Display the uploaded image
            uploaded_image = Image.open(file_upload)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            image_io = io.BytesIO()
            uploaded_image.save(image_io, format='PNG')
            image_bytes = image_io.getvalue()
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')  # Encode as base64
            response = detect_text(image_base64)  # Image data is in base64

            if "error" in response:
                st.error(f"Error: {response['error']['message']}")
            else:
                text_annotations = response['responses'][0].get('fullTextAnnotation', {})
                extracted_text = text_annotations.get('text', '')

                st.subheader("Extracted Text from Image:")
                st.write(extracted_text)

                # Add download button for extracted text
                st.download_button(
                    label="Download Text file",
                    data=extracted_text,
                    key="download",
                    on_click=None,
                    args=("extracted_text.txt",),
                )
