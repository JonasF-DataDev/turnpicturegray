import streamlit as st
from PIL import Image
import io # voor het omgaan met byte-objecten

st.title("Gray image convertor")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

# Bestand uploaden
upload_image = st.file_uploader("Upload Image")

# Functie om een afbeelding om te zetten naar een downloadbaar object
def get_image_download_button(image, filename="grayscale_image.png"):
    # Opslaan van de afbeelding in bytes
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Wanneer er een afbeelding wordt geüpload
if upload_image:
    img = Image.open(upload_image)

    # Converteren naar grijstinten
    gray_img = img.convert("L")

    # Afbeelding tonen
    st.image(gray_img)

    # Download button toevoegen
    buffer = get_image_download_button(gray_img)
    st.download_button(label="Download Gray Image",
                       data=buffer,
                       file_name="grayscale_image.png",
                       mime="image/png")


#if camera_image = true zorgt ervoor dat de code enkel wordt uitgevoerd wanneer er een camera image is
if camera_image:

    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render/Display grayscale image on webpage
    st.image(gray_img)

    # Download button toevoegen
    buffer = get_image_download_button(gray_img)
    st.download_button(label="Download Gray Image",
                       data=buffer,
                       file_name="grayscale_image.png",
                       mime="image/png")