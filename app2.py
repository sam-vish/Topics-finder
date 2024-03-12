# Load the environment variables
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")


import streamlit as st
from langchain.schema import SystemMessage
from langchain.chat_models import ChatOpenAI

# Streamlit UI
st.set_page_config(page_title="Topic Generator")
st.header("Welcome to Topic Generator!")

# Initialize Langchain model
chat = ChatOpenAI(openai_api_key=api_key)

# Function to generate topics related to the input
def generate_topics(input_topic, num_topics=3):
    
    prompt = f"Generate {num_topics} topics related to {input_topic}."
    
    topics_response = chat([SystemMessage(content=prompt)])
    topics = topics_response.content.split("\n")[:num_topics]
    return topics

# Function to summarize a topic
def summarize_topic(topic):
    prompt = f"Summarize the topic: {topic}"
    response = chat([SystemMessage(content=prompt)])
    return response.content

# Function to generate code examples related to a topic
def generate_code_examples(topic):
    prompt = f"Generate code examples related to the topic: {topic}"
    response = chat([SystemMessage(content=prompt)])
    return response.content

# Function to create a quiz question for a topic
def create_quiz_question(topic):
    prompt = f"Create a quiz question for the topic: {topic}"
    response = chat([SystemMessage(content=prompt)])
    return response.content

# Get user input
input_topic = st.text_input("Enter a topic:", "FastAPI")

# Generate topics when user clicks the button
if st.button("Generate Topics"):
    topics = generate_topics(input_topic)
    st.subheader("Related Topics:")
    for i, topic in enumerate(topics, 1):
        st.write(f"{topic}")

    st.subheader("Summaries of Topics:")
    for topic in topics:
        summary = summarize_topic(topic)
        st.write(f"- Summary of {topic}: {summary}")

    st.subheader("Code Examples of Topics:")
    for topic in topics:
        code_examples = generate_code_examples(topic)
        st.write(f"- Code examples related to {topic}: {code_examples}")

    st.subheader("Quiz Questions:")
    for topic in topics:
        quiz_question = create_quiz_question(topic)
        st.write(f"- Quiz question for {topic}: {quiz_question}")
