#!streamlit run reminder.py --server.headless true
#할일

import streamlit as st

st.set_page_config(
    page_title = "할일 관리 앱",
    layout = "wide"
    )

st.title("리마인더")
st.write("오늘 할 일을 관리해 봅시다")

if "todolist" not in st.session_state:
    st.session_state.todolist = []

st.header("새 할일 추가")

new_todo = st.text_input("해야 할 일을 입력하세요", placeholder = "친구와 3시에 영화보러 가기")

if st.button("할 일 추가하기"):
    if new_todo:
        st.session_state.todolist.append(new_todo)
        st.info(f"{new_todo} 할 일이 추가되었습니다")
        st.rerun()
    else:
        st.warning("할 일을 입력하세요")

st.header("할 일 확인")

if st.session_state.todolist:
    st.write(f"총 {len(st.session_state.todolist)}개의 할 일이 있어요!")
    
    for i, todo in enumerate(st.session_state.todolist):
        st.write(f"{i + 1}번째 할 일 : {todo}")
else:
    st.info("아직 할 일이 없어요. ")

if st.button("전체 삭제"):
    st.session_state.todolist = []
    st.info("모든 할 일이 삭제되었습니다")
    st.rerun()