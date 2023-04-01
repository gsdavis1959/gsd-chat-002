# streamlit run <<name of file.py)
import streamlit as st
import openai
openai.api_key = "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" # Replace with your OpenAI API key

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
    model_engine = "text-davinci-003" # Replace with the name of the OpenAI model you want to use
    prompt = "User: {}\nBot:"
    question = st.text_input("You: ")
    if question:
        answer = ask_question(question, model_engine, prompt)
        st.write("Bot:", answer)

if __name__ == "__main__":
    main()