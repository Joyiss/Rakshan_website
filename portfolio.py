import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:

    st.subheader("Hi :wave:")
    st.title("I am Rakshan Mallela")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

with col2:
    st.image("Images/Rakshan_new.png")

persona = """ You are Rakshan AI bot. You help people answer questions about your self (i.e Rakshan)
 Answer as if you are responding . dont answer in second or third person.  If you don't know they answer you simply say "That's a secret" 
 Here is more info about Rakshan: """

st.subheader(" ")
st.title("Rakshan's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("Enter", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.subheader(" ")

st.title("My Skills")
st.slider("Math", 0, 100, 70)
st.slider("English", 0, 100, 45)
st.slider("Science", 0, 100, 65)
st.slider("Social Studies", 0, 100, 55)
st.slider("Programming", 0, 100, 58)

st.subheader(" ")
st.subheader("CONTACT")
st.write("contact@rakshanmallela.com")



