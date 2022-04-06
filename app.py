#Load libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings

# Import helpers
import sys
sys.path.insert(1, 'scripts/')
from helpers import get_image_names, plotSimilarImages

import os
import pickle
import shutil

warnings.filterwarnings("ignore")

#Set title and favicon
st.set_page_config(page_title=' Personalized Ad Recommendations', page_icon='https://upload.wikimedia.org/wikipedia/commons/e/e6/Duke_University_logo.svg')

###################### CSS Styling ############################################################################################################
# Hide rainbow bar
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Hide hamburger menu & footer
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

#Credit to: https://discuss.streamlit.io/t/how-to-set-file-download-function/2141
def get_table_download_link(df):
    """
    Generates a link allowing the data in a given dataframe to be downloaded.
    
    Parameters
    ----------
    df: dataframe
            Dataframe to download.
    
    Output
    ----------
    out: str
        href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="personalized_recommendations.csv">Download CSV</a>'

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
        fig = plotSimilarImages(image, similarNames, similarValues, inputDir = "images_only2")
        st.pyplot(fig)

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
    
    #Review the raw data (dataframe) in the app
    if st.checkbox('Show File With Recommendations', False): #Creates a checkbox to show/hide the data
        st.write(df_matches)

        #Allow users to download the data
        st.markdown(get_table_download_link(df_matches), unsafe_allow_html=True)


