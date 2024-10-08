import streamlit as st
import json
from datetime import datetime
from sheets import insert_row


def get_questions():
    with open('questions.json', 'r') as f:
        data = json.load(f)
    return data


def main():
    data = get_questions()
   
    st.title("Academic Stress Survey")

    st.header("Demographics")
    name = st.text_input("Name", value=None)
    age = st.number_input("Age", min_value=0, max_value=100, value=None)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=None)
    birth_order = st.selectbox("Birth Order", ["First Born", "Second Born", "Third Born", "Only Child"], index=None)
    education = st.selectbox("Education Level", ["High School", "Undergraduate", "Graduate", "Postgraduate"], index=None)
    family_type = st.selectbox("Family Type", ["Nuclear", "Joint", "Single Parent", "Other"], index=None)
    school = st.selectbox("School", ["SAS", "SSL", "SCOPE", "SELECT", "SENSE", "SMEC", "SCE", "VITBS", "VITSOL", "VFIT"], index=None)
    batch = st.selectbox("Batch", [2020, 2021, 2022, 2023, 2024], index=None)
    
    
    st.header("Questions")
    responses = {}

    for question in data['questions']:
        response = st.radio(question['question'], question['options'], index=None)
        responses[question['id']] = response

    if st.button("Submit"):
        if "" in [age, gender, birth_order, education, family_type, school, batch] or "" in responses.values() or None in responses.values():
            st.error("Please answer all questions before submitting.")
        else:
            row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, age, gender, birth_order, education, family_type, school, batch] + list(responses.values())
            insert_row(row)
            st.success("Thank you for completing the survey! Your responses have been recorded.")


if __name__ == "__main__":
    main()