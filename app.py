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
@font-face {
font-family: 'Tangerine';
font-style: normal;
font-weight: 400;
src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

html, body, [class*="css"]  {
font-family: 'Tangerine';
font-size: 48px;
}
</style>

""",
    unsafe_allow_html=True)

###################### CSS Styling ############################################################################################################



#Create initial titles/subtitles
st.markdown('<h1 style="font-family:Avenir,Helvetica Neue,sans-serif;"> Personalized Ad Recommendations </h1>', unsafe_allow_html=True)
st.text("")
st.markdown('<p style="font-family:Avenir,Helvetica Neue,sans-serif;">Lorem Ipsum</p>', unsafe_allow_html=True)

