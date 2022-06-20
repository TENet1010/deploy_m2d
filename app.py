import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from readimage import gen_night2day


def load_image(image_file):
	img = Image.open(image_file)
	return img

night2day = False
st.title("Image transfer")

menu = ["day to Night","Night to day"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "day to Night":
    st.subheader("day to Night")

elif choice == "Night to day":
    st.subheader("Night to day")
    night2day = True

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file:
    load_im = load_image(image_file)
    st.image(load_im,width=300)
    result = gen_night2day(np.array(load_im),Night2day = night2day)
    st.write('result')
    st.image(result,width=300)


