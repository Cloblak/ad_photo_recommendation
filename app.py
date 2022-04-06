#Load libraries
import tldextract
import streamlit as st
import pandas as pd
import numpy as np
import wget
import base64
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
import zipfile

import os
import pickle
import shutil
from PIL import Image

warnings.filterwarnings("ignore")

#Set title and favicon
st.set_page_config(page_title=' Personalized Ad Recommendations', page_icon='https://upload.wikimedia.org/wikipedia/commons/e/e6/Duke_University_logo.svg')

###################### CSS Styling ############################################################################################################
#Hide rainbow bar
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

#Hide hamburger menu & footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#General font (body)
st.markdown(
  """
  <style>
    body {
    font-family: Manrope;
    }
  </style>""",
  unsafe_allow_html=True
)

###################### CSS Styling ############################################################################################################

st.markdown('<h1 style="font-family:Manrope;"> Personalized Ad Recommendations</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-family:Manrope;">Lorem Ipsum</p>', unsafe_allow_html=True)

zipped_folder = st.file_uploader("Upload your zipped folder", type="zip")
if zipped_folder is not None:
    zipped_folder = zipfile.ZipFile(zipped_folder)


#with zipfile.ZipFile(zipped_folder, 'r') as zip_ref:
#    zip_ref.extractall('query_images')

#st.write(zipped_folder)

