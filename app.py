# streamlit run <<name of file.py)
import streamlit as st
import openai
import os

openai.api_key = os.getenv('API_KEY') # Replace with your OpenAI API key

if "messages" not in st.session_state:
    st.session_state.messages = []
    
def ask_question(question, model_engine, prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.format(question),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.title("Chatbot")
    model_engine = "gpt-4o" # Replace with the name of the OpenAI model you want to use
    prompt = "User: {}\nBot:"
    question = st.text_input("You: ")
    if question:
        answer = ask_question(question, model_engine, prompt)
        st.write("Bot:", answer)

    if st.button("Clear Chat History"):
        st.session_state.messages.clear()
        st.runtime.legacy_caching.clear_cache()
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi there. Can I help you?"}]


if __name__ == "__main__":
    main()
