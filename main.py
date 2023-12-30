import google.generativeai as genai
import streamlit as st

genai.configure(api_key='AIzaSyB8x5oCVBSRZiuNxAUgodiNxdPRYUhEwY8')

model = genai.GenerateModel('gemini-pro')
chat = model.start_chat(history = [])

def get_response(question):
    response = chat.send_message(question,stream = True)
    return response


st.set_page_config('J.A.R.W.I.S.')

st.header('J.A.R.W.I.S. AI')

st.snow()

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input('Input',key='input')
button=st.button('Ask the question')

if input and button:
    response = get_response(input)
    st.session_state['chat_history'].append(('You',input))
    st.subheader('Response is')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))

st.subheader('The chat history is')

for role,text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')

