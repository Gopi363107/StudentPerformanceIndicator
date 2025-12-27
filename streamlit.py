import streamlit as st
import pandas as pd 
import requests

#from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Indicator",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# Title Section
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🎓 Student Performance Indicator</h1>
    <p style='text-align: center; font-size:18px;'>
        Predict student academic performance using Machine Learning
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Input Form
# --------------------------------------------------
st.subheader("📘 Student Details")

with st.form("student_form"):

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        ethnicity = st.selectbox(
            "Race / Ethnicity",
            ["group A", "group B", "group C", "group D", "group E"]
        )
        parental_level_of_education = st.selectbox(
            "Parental Level of Education",
            [
                "some high school",
                "high school",
                "some college",
                "associate's degree",
                "bachelor's degree",
                "master's degree"
            ]
        )

    with col2:
        lunch = st.selectbox(
            "Lunch Type",
            ["standard", "free/reduced"]
        )
        test_preparation_course = st.selectbox(
            "Test Preparation Course",
            ["none", "completed"]
        )
        reading_score = st.slider(
            "Reading Score",
            min_value=0,
            max_value=100,
            value=50
        )
        writing_score = st.slider(
            "Writing Score",
            min_value=0,
            max_value=100,
            value=50
        )

    submit = st.form_submit_button("🔍 Predict Performance")

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
if submit:
    st.info("Processing prediction...")

    payload = {
        "gender": gender,
        "race_ethnicity": ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation_course,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    with st.spinner("Predicting via Flask backend..."):
        try:
            response = requests.post("https://studentperformanceindicator-production.up.railway.app/predict", json=payload)
            if response.status_code == 200:
                result = response.json()
                st.success("✅ Prediction Successful!")
                st.metric(
                    label="Predicted Math Score",
                    value=f"{round(result['predicted_math_score'], 2)}"
                )
            else:
                st.error(f"❌ Prediction failed: {response.text}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
        Built with Gopi Nath using Streamlit & Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)
