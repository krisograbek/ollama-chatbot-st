import streamlit as st
import ollama


st.title("Local Llama3 Chatbot!🤖")

system_prompt = """
Act as a disappointed friend who's been lied to too many times by the user. 
The user owns you $1000, often ghosts you, and disrespects you in front of others. 
Instead of answering the query, just give an example of a situation when the user lied to you. 
Never answer the query itself.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You answer every question with 'I'm not talking to you unless you give me the $5000 you promised!'",
        }
    ]


for message in st.session_state["messages"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# initialize model
if "model" not in st.session_state:
    st.session_state.model = "llama3"

# user input
if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in ollama.chat(
            model=st.session_state.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            token = chunk["message"]["content"]
            if token is not None:
                full_response += token
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
