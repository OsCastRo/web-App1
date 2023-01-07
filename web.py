import streamlit as st
import FUNCTIONS

tasks = FUNCTIONS.get_tasks()

def add_task():
    todo = st.session_state["new_todo"] + "\n"
    tasks.append(todo)
    FUNCTIONS.write_tasks(tasks)


st.title("My Todo App")
st.subheader("This is my todo app")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        FUNCTIONS.write_tasks(tasks)
        del st.session_state[task]
        st.experimental_rerun()


st.text_input(label = "", placeholder="add new task",
              on_change=add_task, key="new_todo")
