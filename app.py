import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Indicator",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# Title
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
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        test_preparation_course = st.selectbox(
            "Test Preparation Course",
            ["none", "completed"]
        )
        reading_score = st.slider("Reading Score", 0, 100, 50)
        writing_score = st.slider("Writing Score", 0, 100, 50)

    submit = st.form_submit_button("🔍 Predict Performance")

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
if submit:
    with st.spinner("Predicting student performance..."):
        try:
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            input_df = data.get_data_as_data_frame()

            pipeline = PredictPipeline()
            prediction = pipeline.predict(input_df)

            predicted_score = round(float(prediction[0]), 2)

            st.success("✅ Prediction Successful!")
            st.metric("Predicted Math Score", predicted_score)

        except Exception as e:
            st.error(f"❌ Error occurred: {e}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
        Built by Gopi Nath using Streamlit & Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)
