# import os
# from dotenv import load_dotenv
# import streamlit as st
# import google.generativeai as genai

# # Load env variables
# load_dotenv()

# # Configure API
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.0-flash")

# # Page config
# st.set_page_config(page_title="Chatbot", page_icon="🤖")

# st.title("Your Personal Chatbot")
# st.write("Ask me anything!")

# # Session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Input
# user_input = st.chat_input("Type your message here...")

# # Handle input
# if user_input:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input
#     })

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             try:
#                 history = [
#                     {"role": m["role"], "parts": [m["content"]]}
#                     for m in st.session_state.messages[:-1]
#                 ]

#                 chat = model.start_chat(history=history)
#                 response = chat.send_message(user_input)

#                 ai_message = response.text

#                 st.markdown(ai_message)

#                 st.session_state.messages.append({
#                     "role": "assistant",
#                     "content": ai_message
#                 })

#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load env variables
load_dotenv()

# Setup Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Page config
st.set_page_config(page_title="Chatbot", page_icon="🤖")

st.title("Your Personal Chatbot")
st.write("Ask me anything!")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
user_input = st.chat_input("Type your message here...")

# Handle input
if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Convert history directly (Groq uses OpenAI format)
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",  # FREE model
                    messages=st.session_state.messages
                )

                ai_message = response.choices[0].message.content

                st.markdown(ai_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_message
                })

            except Exception as e:
                st.error(f"Error: {str(e)}")