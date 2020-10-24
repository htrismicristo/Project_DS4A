import app1
import app2
import streamlit as st
from PIL import Image

# Set the sidebar color
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#ED1B24, #ED1B24);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# Set the sidebar image
image = Image.open("./CI_logo.png")
st.sidebar.image(image, use_column_width=True)

# Set the sidebar title
st.sidebar.title('Ceramica Italia web app')

# Set the sidebar selectbox for choosing dashboard
PAGES = {
    "Customer Segmentation": app1,
    "Google Analytics": app2
}
st.sidebar.subheader("Select a dashboard page")
selection = st.sidebar.selectbox("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# Set author names on the sidebar using markdown
st.sidebar.markdown(

    """
AUTHORS:

NATALÍ VELASQUEZ\n
DANIEL ESCAMILLA\n
DANNIN GOMEZ\n
DAVID NAVARRO\n
FREDY MUÑOZ\n
HERMES ROMERO\n
WILSON RODRÍGUEZ\n


""")
