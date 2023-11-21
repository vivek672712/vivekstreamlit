import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("student data ")

df=pd.read_csv('student.csv')
x=df["age"]
y=df["sex"]
if st.sidebar.button("show data"):
    st.write(df)


if st.sidebar.button("show chart"):
    plt.xlabel("age")
    plt.ylabel("sex")
    plt.bar(x,y)
    plt.show()
