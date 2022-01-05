#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:16:33 2022

@author: fablab
"""

import pandas as pd
import datetime
import streamlit as st

st.set_page_config(layout = "wide")

def ChangeMonth(text):
    dict_replacements = {
        "January": "Enero",
        "February": "Febrero",
        "March": "Marzo",
        "April": "Abril",
        "May": "Mayo",
        "June": "Junio",
        "July": "Julio",
        "August": "Agosto",
        "September": "Septiembre",
        "October": "Octubre",
        "November": "Noviembre",
        "December": "Diciembre"
        }
    for word in dict_replacements.keys():
        text = text.replace(word, dict_replacements[word])
    
    return text




data = pd.read_csv("data_shows_2022.csv")
data = data.sort_values("next_episode")
data_providers = pd.read_csv("info_providers.csv")
col1, col2,col3 = st.columns([2,2,10])
with col1:
    st.image("https://img.icons8.com/clouds/100/000000/retro-tv.png")
    
with col2:
    st.write("""
             # ¿Qué vemos hoy?
             """)
    selected = st.checkbox("Mobile version", value = True)
with col3:
    st.write("Los próximos shows en las plataformas son:")
    choice = st.number_input("Número de shows", 0,10,5)
    


for i in range(choice):
    
    if selected:
        col1_1, col1_4, col1_2 = st.columns([2,4,20])
        col1_3,col1_6 = st.columns([8,1])
        col1_5,col1_7 = st.columns(2)
    else:
        col1_1, col1_2, col1_4,col1_3,col1_5,col1_6  = st.columns([2,3,3,10,4,1])
    
    with col1_1:
        st.image(data.poster[i])
    with col1_2:
        date_next = datetime.datetime.strptime(data.next_episode[i], "%Y-%m-%d")
        date_next_str = date_next.strftime("%d de %B")
        date_next_str = ChangeMonth(date_next_str)
        st.subheader(date_next_str)
    with col1_4:
        st.subheader(data.name[i])
    with col1_3:
        st.write(data.overview[i])
    with col1_6:
        provider = data_providers[data_providers.provider_id == data.id_platform[i]].reset_index()
        url_provider = "https://www.themoviedb.org/t/p/original" + provider["logo_path"][0]
        st.image(url_provider)
    with col1_5:
        if type(data.trailer_url[i]) == str:
            st.video(data.trailer_url[i])
        else:
            st.image("https://img.icons8.com/ios-filled/50/000000/image-not-avialable.png")
            