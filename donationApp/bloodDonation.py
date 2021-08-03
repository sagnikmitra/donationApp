import streamlit as st
from PIL import Image
import sys
import pyodbc as odbc

import base64

records = []
DRIVER = "ODBC Driver 17 for SQL Server"
SERVER_NAME = "MEENU\SQLEXPRESS"
DATABASE_NAME="StreamLit"
cnxn = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
"""

def bloodDonate() :
    st.title("Blood Donation")
    main_bg = "blood.gif"
    main_bg_ext = "gif"
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

    img = Image.open("_bloodDonation.jpg")
    st.image(img, caption='Blood Donation', width=500)
    st.write("This is the blood donation page.")
    st.write("Here if you are willing to donate blood\n you have to register yourself.")
    
    with st.form(key="Registration for Blood Donation"):
        bloodname = st.text_input("Enter your name : ")
        bgrp = st.text_input("Enter your blood group : ")
        age = st.slider(label="Enter your age ", min_value=18, max_value=45)
        blood_phone =  st.text_input("Enter your Phone number : ")
        date = st.date_input(label="Date")
        
        submissionblood = st.form_submit_button(label="Submit")
        if submissionblood==True:
            addData(bloodname,bgrp,age,blood_phone,date)

            

def addData(a,b,c,d,e):
    
    conn = odbc.connect(cnxn)
    cursor = conn.cursor()
    
    cursor.execute(" INSERT INTO Blood_Donation VALUES (?, ?, ?, ?, ?);", (a,b,c,d,e))
    st.success("Successfully inserted")
    #cursor.commit()
    cursor.close()

    


    #adding date picker..

