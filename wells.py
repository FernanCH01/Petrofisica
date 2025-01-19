# Import Python Libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from pathlib import Path
import lasio
import welly



#icono
icon = Image.open('logo/icono.jpg')

st.set_page_config(page_title="Petrophysics App", page_icon=icon)
