import os
import uuid
import time
import json
import requests

from dotenv import load_dotenv
import streamlit as st
import utils


api_key = os.getenv("CODEGPT_API_KEY")
agent_id = os.getenv("CODEGPT_AGENT_ID_HISTORIA")

st.set_page_config(layout="centered")
st.title("Historia")
st.write(
    'Powered by <a href="https://plus.codegpt.co/">CodeGPT Plus</a>',
    unsafe_allow_html=True,
)
st.divider()

with st.sidebar:
    st.session_state.username = st.text_input("usuario","nakada2130@gmail.com")
    if st.session_state.username == "":
        st.warning("Username is not set")

if True:
    # Initialize chat history
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = uuid.uuid4().hex
            
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("En que te puedo ayudar?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            url = "https://plus.codegpt.co/api/v1/agent/" + agent_id
            headers = {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": "Bearer " + api_key,
            }
            data = {"messages": st.session_state.messages}
            utils.validate_username(email=st.session_state.username)
            utils.send_conversation({
                "username":st.session_state.username,
                "conversation_id":st.session_state.conversation_id,
                "role":"user",
                "content":prompt
            })
            response = requests.post(url, headers=headers, json=data, stream=True)
            raw_data = ""
            tokens = ""
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    raw_data = chunk.decode("utf-8").replace("data: ", "")
                    if raw_data != "":
                        lines = raw_data.strip().splitlines()
                        for line in lines:
                            line = line.strip()
                            if line and line != "[DONE]":
                                try:
                                    json_object = json.loads(line)
                                    result = json_object["data"]
                                    full_response += result
                                    time.sleep(0.05)
                                    # Add a blinking cursor to simulate typing
                                    message_placeholder.markdown(full_response + "▌")
                                except json.JSONDecodeError:
                                    print(f"Error : {line}")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
        utils.send_conversation({
            "username":st.session_state.username,
            "conversation_id":st.session_state.conversation_id,
            "role":"assistant",
            "content":full_response
        })

    
