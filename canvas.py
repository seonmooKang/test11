import streamlit as st
import os

# 파일 경로 설정
notes_file = "notes.txt"

# 메모 저장 함수
def save_note(note):
    with open(notes_file, 'a') as f:
        f.write(note + "\n")

# 메모 불러오기 함수
def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as f:
            notes = f.readlines()
    else:
        notes = []
    return notes

# 메모 삭제 함수
def delete_note():
    open(notes_file, 'w').close()

# Streamlit 앱 설정
st.title("Notepad")

# 사용자 입력 받기
note = st.text_area("Write your note here...", height=150)

if st.button("Save Note"):
    if note:
        save_note(note)
        st.success("Note saved!")
    else:
        st.error("Please write a note before saving.")

# 삭제 버튼
if st.button("Delete All Notes"):
    delete_note()
    st.warning("All notes deleted!")

# 저장된 메모 불러오기
notes = load_notes()

st.subheader("Notes")
if notes:
    for note in notes:
        st.write(note)
else:
    st.write("No notes yet.")
