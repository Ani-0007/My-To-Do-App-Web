# streamlit run web.py
# Imports
import streamlit as st
import functions

todos = functions.read_todo()


# Functions
def add_todo():
    todo = st.session_state["newtodo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


# Interface
st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to track your daily activities.")

for index, items in enumerate(todos):
    checkbox = st.checkbox(items, key=items)
    if checkbox is True:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[items]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new To-do...",
              on_change=add_todo, key="newtodo")