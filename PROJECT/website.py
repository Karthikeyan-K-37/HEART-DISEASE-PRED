import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
heart=pickle.load(open('data.sav','rb'))

with st.sidebar:
    selected=option_menu('MENU',['HEART DISEASE'],icons=['heart-pulse','gear'])

if(selected == 'HEART DISEASE' ):
    st.title('HEART DISEASE PREDICTION')
    col1,col2 = st.columns(2)
    with col1:
        Age=st.text_input('AGE OF THE PERSON')
    with col2:
        Sex=st.text_input('GENDER OF THE PERSON')
    with col1:
        Chest_pain_type=st.text_input('TYPE OF CHEST PAIN')
    with col2:
        BP=st.text_input('BP LEVEL')
    with col1:
        Cholesterol=st.text_input('CHOLESTEROL LEVEL')
    with col2:
        FBS_over_120=st.text_input('IS FBS OVER 120')
    with col1:
        EKG_results=st.text_input('EKG RESULTS')
    with col2:
        Max_HR=st.text_input('MAX_HR')
    with col1:
        Exercise_angina=st.text_input('EXERCISE ANGINA')
    with col2:
        ST_depression=st.text_input('ST DEPRESSION')
    with col1:
        Slope_of_ST=st.text_input('SLOPE OF ST')
    with col2:
        vessels=st.text_input('NUMBER OF VESSELS IN FLURO')
    with col1:
        Thallium=st.text_input('THALLIUM LEVEL')
    


    HEART_DIGNOSIS=' '

    if st.button('HEART DISEASE RESULT'):
        heart_prediction=heart.predict([[int(Age),int(Sex),int(Chest_pain_type),int(BP),int(Cholesterol),int(FBS_over_120),int(EKG_results),int(Max_HR),int(Exercise_angina),float(ST_depression),int(Slope_of_ST),int(vessels),int(Thallium)]])
        if (heart_prediction == 'Presence' ):
            HEART_DIGNOSIS='THE PERSON HAS HEART PROBLEM'
        else:
            HEART_DIGNOSIS='THE PERSON DOES NOT HAVE HEART PROBLEM'
    st.success(HEART_DIGNOSIS)





 