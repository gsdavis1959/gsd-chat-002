# streamlit run <<name of file.py)
import streamlit as st
import openai
import os

openai.api_key = os.getenv('API_KEY') # Replace with your OpenAI API key

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Display previous messages
if st.session_state.messages:
    for msg in st.session_state.messages:
        if msg["user"]:
            st.write(f"You: {msg['content']}")
        else:
            st.write(f"GPT-4: {msg['content']}")

# Text input for the user's message
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        # Save user's message
        st.session_state.messages.append({"user": True, "content": user_input})
        
        # Generate GPT-4 response
        gpt_response = generate_response(user_input)
        
        # Save GPT-4's response
        st.session_state.messages.append({"user": False, "content": gpt_response})
        
        # Display the response
        st.write(f"GPT-4: {gpt_response}")
