import streamlit as st
import pandas as pd
import pickle

df=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommendation(title):
    idx=df[df['Title']==title].index[0]
    idx=df.index.get_loc(idx)
    distances=sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:20]
    jobs=[]
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)

    return jobs
#web app

st.title('Job Recommendation System')
name=st.text_input("Enter Your Name")
edu=st.text_input("Education")
Exp=st.text_input("Years of Experience")
skills=st.text_input("Skills")
title= st.selectbox('Enter Job Position',df['Title'],disabled=False)

jobs = recommendation(title)
if st.button("Recommend Job", on_click=None,type="secondary", disabled=False):
    if jobs:
        st.write(jobs)