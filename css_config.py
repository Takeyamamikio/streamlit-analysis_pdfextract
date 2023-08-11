import streamlit as st


def hide_hamburgermenu():
    """Oculta o menu hamburger no topo direito"""
    st.markdown(
        """<style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style> """, unsafe_allow_html=True)


def remove_toppadding():
    st.markdown(
        """<style>
            .appview-container .main .block-container {{
                padding-top: {padding_top}rem;
                padding-bottom: {padding_bottom}rem;}}
        </style>"""
        .format(padding_top=1, padding_bottom=1),
        unsafe_allow_html=True,)


def add_bg_from_url(bg_url):
    # bg_url = 'https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg'
    st.markdown(
        f"""<style>
            .stApp {{
                background-image: url({bg_url});
                background-attachment: fixed;
                background-size: cover}}
        </style>""", unsafe_allow_html=True)


def add_bg_from_local(image_file):
    import base64
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""<style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover}}
        </style>""", unsafe_allow_html=True)