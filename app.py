import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Kidney Disease Prediction")

# Inputs for all columns
age = st.number_input("Age")
bp = st.number_input("Blood Pressure")
sg = st.number_input("Specific Gravity")
al = st.number_input("Albumin")
su = st.number_input("Sugar")

rbc = st.selectbox("Red Blood Cells (0=abnormal, 1=normal)", [0,1])
pc = st.selectbox("Pus Cell (0=abnormal, 1=normal)", [0,1])
pcc = st.selectbox("Pus Cell Clumps (0=no, 1=yes)", [0,1])
ba = st.selectbox("Bacteria (0=no, 1=yes)", [0,1])

bgr = st.number_input("Blood Glucose Random")
bu = st.number_input("Blood Urea")
sc = st.number_input("Serum Creatinine")

sod = st.number_input("Sodium")
pot = st.number_input("Potassium")

hemo = st.number_input("Hemoglobin")
pcv = st.number_input("Packed Cell Volume")
wc = st.number_input("White Blood Cell Count")
rc = st.number_input("Red Blood Cell Count")

htn = st.selectbox("Hypertension (0=no, 1=yes)", [0,1])
dm = st.selectbox("Diabetes Mellitus (0=no, 1=yes)", [0,1])
cad = st.selectbox("Coronary Artery Disease (0=no, 1=yes)", [0,1])

appet = st.selectbox("Appetite (0=poor, 1=good)", [0,1])
pe = st.selectbox("Pedal Edema (0=no, 1=yes)", [0,1])
ane = st.selectbox("Anemia (0=no, 1=yes)", [0,1])

# Prediction button
if st.button("Predict"):

    data = {
        "Age": age,
        "Blood Pressure": bp,
        "Specific Gravity": sg,
        "Albumin": al,
        "Sugar": su,
        "Red Blood Cells": rbc,
        "Pus Cell": pc,
        "Pus Cell Clumps": pcc,
        "Bacteria": ba,
        "Blood Glucose Random": bgr,
        "Blood Urea": bu,
        "Serum Creatinine": sc,
        "Sodium": sod,
        "Potassium": pot,
        "Hemoglobin": hemo,
        "Packed Cell Volume": pcv,
        "White Blood Cell Count": wc,
        "Red Blood Cell Count": rc,
        "Hypertension": htn,
        "Diabetes Mellitus": dm,
        "Coronary Artery Disease": cad,
        "Appetite": appet,
        "Pedal Edema": pe,
        "Anemia": ane
    }

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    if prediction[0] == "ckd":
        st.error("Kidney Disease Detected ❌")
    else:
        st.success("No Kidney Disease ✅")