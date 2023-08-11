import streamlit as st
import os
from io import BytesIO
from css_config import *
from pdf_extractor import extract

st.set_page_config(page_title="Extrator de pdf",
                   page_icon=":test_tube:",  # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
                   layout="wide",  # wide ou centered
                   initial_sidebar_state="expanded",  # "auto", "expanded", ou "collapsed"
                   menu_items={'Get Help': 'https://www.extremelycoolapp.com/help',
                               'Report a bug': "https://www.extremelycoolapp.com/bug",
                               'About': "# Aplicativo desenvolvido por *Matheus Mikio Takeyama*"})

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def to_excel(df):
    in_memory_fp = BytesIO()
    df.to_excel(in_memory_fp, index=False)
    # Write the file out to disk to demonstrate that it worked.
    in_memory_fp.seek(0, 0)
    return in_memory_fp.read()

hide_hamburgermenu()
remove_toppadding()
add_bg_from_local('files/background/background1.jpg')

if 'banner' not in st.session_state:
    st.session_state['banner'] = 'banner1'

##############################
# --- Início da interface ---#
##############################
l_pad, center, r_pad = st.columns([1, 2, 1])

center.image(f"files/banner/{st.session_state['banner']}.jpg")

l_pad2, center2, r_pad2 = center.columns([1, 2, 1])
st.session_state['banner'] = center2.radio('Background', ['banner1', 'banner2', 'banner3'], index=1, horizontal=True, label_visibility='hidden')

center.title('Extrator de pdf')

file = center.file_uploader('Arquivo pdf', label_visibility='hidden')

dataframe = center.empty()
dw_btn = center.empty()
if file is not None:
    file_name, _extention = os.path.splitext(file.name)
    df = extract(file)
    excel = to_excel(df)
    dataframe = center.table(df)
    dw_btn.download_button('download', excel, f'{file_name}.xlsx', f'{file_name}.xlsx', key=f'{file_name}.xlsx')