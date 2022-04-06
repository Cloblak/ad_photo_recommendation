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

# Import helpers
import sys
sys.path.insert(1, 'scripts/')
import helpers
from helpers import get_image_names, setAxes, getSimilarImages, plotSimilarImages

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

### Helpers ###

def save_uploadedfile(uploadedfile):
    """
    Save a file to the local directory.

    Parameters
    ----------
    uploadedfile : 
            File to save.
    """
    with open(os.path.join(uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())

###############

st.markdown('<h1 style="font-family:Manrope;"> Personalized Ad Recommendations</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-family:Manrope;">Lorem Ipsum</p>', unsafe_allow_html=True)

# Load models
with open('similarNames.pkl', 'rb') as handle:
    similarNames = pickle.load(handle)

with open('similarValues.pkl', 'rb') as handle:
    similarValues = pickle.load(handle)

zipped_folder = st.file_uploader("Upload your zipped folder", type="zip")

# Save & Unzip the file
if zipped_folder is not None:
    file_details = {"FileName":zipped_folder.name,"FileType":zipped_folder.type}
    save_uploadedfile(zipped_folder)
    shutil.unpack_archive(zipped_folder.name, 'query_images')

    qry_img_list = get_image_names('query_images')
    URL_dict = pd.read_csv('images_CO.csv').set_index('Image_Name').to_dict()

    # Plot recommended images
    for image in qry_img_list:
        st.pyplot(plotSimilarImages(image, similarNames, similarValues, inputDir = "images_only2"))

    # Create a dictionary with all of the recommendations
    matches = {}
    for query_image in qry_img_list:
        URL_recos = []
        for item in list(similarNames.loc[query_image, :]):
            URL_recos.append(URL_dict['URL'][item])
        matches[query_image] = URL_recos

    # Convert from Dict to DF
    df_matches = pd.DataFrame.from_dict(matches, orient='index')
    df_matches.columns = ["rec_"+str(x) for x in df_matches.columns]
    df_matches.reset_index(inplace=True)
    df_matches.to_csv("recommendations.csv")
    st.write(df_matches.head())


