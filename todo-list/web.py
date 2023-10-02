import streamlit as st
from modules import functions

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This is a simple todo app to improve your productivity.")
st.write("I'm experimenting with streamlit and python, following udemy course.")

st.write("---")



#display todos as a list of checkboxes
todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a new todo", placeholder="Add a new todo")

