import streamlit as st
import spacy_streamlit

modelo = ['pt_core_news_sm', 'pt_core_news_md','pt_core_news_lg']

texto_padrao = "Marck Zuckeberg é o CEO da Facebook"

spacy_streamlit.visualize(modelo, texto_padrao)