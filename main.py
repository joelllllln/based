from groq import Groq
import pandas as pd
import streamlit as st

st.title('BASED APP')
st.subheader('Who is more based')
st.write("Put your two arugments below and the app will decide which one is more based on evidence and research.")

input1 = st.text_input("Argument 1: ")
input2 = st.text_input("Argument 2: ")
instructions = "you a need to make a decision which is more evidance based adn reasearch, start off with your decision"

def decision(input1, input2):
    client = Groq(api_key="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")  

    response = client.chat.completions.create(
        model="llama3-70b-8192",  
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": f"Argument 1: {input1}\nArgument 2: {input2}"}
        ],
        max_tokens=500
    )
    st.write(response.choices[0].message.content)
    return response

if input1 and input2:  # This is True as soon as both inputs have text
    if st.button("Decide Which Is More Based"):  # This is only True when clicked
        result = decision(input1, input2)  # This only runs when button clicked
        st.write(result)
