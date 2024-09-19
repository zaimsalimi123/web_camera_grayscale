import streamlit as st
from PIL import Image

# Upload an image file
uploaded_image = st.file_uploader("Upload Image")

# Camera input
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a Pillow image instance from the camera input
    img = Image.open(camera_image)
    # Convert the Pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)

elif uploaded_image:
    # Create a Pillow image instance from the uploaded image
    img = Image.open(uploaded_image)
    # Convert the Pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)
