# streamlit run <<name of file.py)
import streamlit as st
import openai
import os

openai.api_key = os.getenv('API_KEY') # Replace with your OpenAI API key


st.title("Simple GPT-4 Chatbot")

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to call the OpenAI API
def get_gpt4_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure you are using the correct model name
            messages=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response['choices'][0]['message']['content'].strip()
        return message
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I couldn't process your request."

# Function to handle user input
def handle_input(user_input):
    st.session_state.messages.append({"role": "user", "content": user_input})
    gpt4_response = get_gpt4_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": gpt4_response})

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        handle_input(user_input)

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Bot:** {message['content']}")
