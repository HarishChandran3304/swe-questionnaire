import streamlit as st
import plotly.graph_objects as go
import json
from sheets import get_all_rows

@st.cache_data
def load_data():
    data = json.load(open('questions.json', 'r'))
    print(data)
    results = []
    for i in range(25):
        question = data['questions'][i]['question']
        options = data['questions'][i]['options']
        responses = [0]*4
        results.append({
            "question": f"Q{i+1}) {question}:",
            "options": options,
            "responses": responses
        })
    responses = get_all_rows()[1:]
    for response in responses:
        for i in range(25):
            match response[i+9]:
                case "Never": results[i]["responses"][0] += 1
                case "Rarely": results[i]["responses"][1] += 1
                case "Often": results[i]["responses"][2] += 1
                case "Always": results[i]["responses"][3] += 1
    
    # Extend the list to 25 questions (for demonstration purposes)
    while len(results) < 25:
        results.append(results[len(results) % 2])
    
    return results

def create_pie_chart(question, options, responses):
    fig = go.Figure(data=[go.Pie(labels=options, values=responses)])
    fig.update_layout(title=f"{question}")
    return fig

def main():
    st.title("MCQ Responses Report")
    
    # Load the cached data
    results = load_data()
    
    st.sidebar.title("Questions")
    selection = st.sidebar.radio("Select a question:", [f"Question {i+1}" for i in range(25)])
    question_index = int(selection.split()[-1]) - 1
    
    question_data = results[question_index]
    
    st.header(f"Total Number of Responses: {sum(question_data['responses'])}")
    st.plotly_chart(create_pie_chart(
        question_data["question"],
        question_data["options"],
        question_data["responses"]
    ))

if __name__ == "__main__":
    main()