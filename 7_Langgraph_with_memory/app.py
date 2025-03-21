import streamlit as st
from transformers import pipeline
from bot import chatbot
from dotenv import load_dotenv
load_dotenv()


mybot = chatbot()
workflow = mybot()

# setup streamlit ui app
st.title("Chatbot with langgraph")
st.write("Ask any question, and I will try to answer")

# Input text box for the question
question = st.text_input("Enter your question here:")
input = {"messages" : [question]}

# Button to get the answer
if st.button("Get Answer"):
    if input:
        response = workflow.invoke(input)
        st.write("**Answer**", response['messages'][-1].content)
    else:
        st.warning("Please enter a question to get an answer")

# Additional styling
st.markdown("---")
st.caption("Powered by Streamlit and Transformers")