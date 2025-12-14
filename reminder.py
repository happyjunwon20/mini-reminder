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
    
if "isdone" not in st.session_state:
    st.session_state.isdone = []

if "Username" not in st.session_state:
    st.session_state.Username = []

if "nowname" not in st.session_state:
    st.session_state.nowname = ""

st.header("이름")
nameinput = st.text_input("이름을 입력하세요")
if st.button("완료"):
    st.session_state.nowname = nameinput
    with open(rf"C:\Users\주원\Desktop\난 최고여\사람들의 리마인더\{st.session_state.nowname}.txt", "w", encoding = "utf-8") as f:
            f.write("")
    if st.session_state.nowname not in st.session_state.Username:
        st.session_state.Username.append(st.session_state.nowname)
        st.session_state.todolist.append([])
        try:
            with open(rf"C:\Users\주원\Desktop\난 최고여\사람들의 리마인더\{st.session_state.nowname}.txt", "r", encoding = "utf-8") as f:
                for lin in f:
                    st.session_state.todolist[st.session_state.Username.index(st.session_state.nowname)].append(lin.rstrip())
        except:
            st.session_state.todolist[st.session_state.Username.index(st.session_state.nowname)] = []

st.header("새 할일 추가")

new_todo = st.text_input("해야 할 일을 입력하세요", placeholder = "친구와 3시에 영화보러 가기")

if st.button("할 일 추가하기"):
    if st.session_state.Username:
        if new_todo:
            st.session_state.todolist[st.session_state.Username.index(st.session_state.nowname)].append(new_todo)
            with open(rf"C:\Users\주원\Desktop\난 최고여\사람들의 리마인더\{st.session_state.nowname}.txt", "w", encoding = "utf-8") as f:
                f.write(new_todo + "\n")
            st.info(f"{new_todo} 할 일이 추가되었습니다")
            st.rerun()
        else:
            st.warning("할 일을 입력하세요")
    else:
        st.error("이름을 입력하세요")

st.header("할 일 확인")
try:
    cols = st.columns(len(st.session_state.todolist))
    for i, thiscol in enumerate(cols):
        with thiscol:
            st.write(f"{st.session_state.Username[i]}님의 할 일")
            if st.session_state.todolist[i]:
                st.write(f"총 {len(st.session_state.todolist[i])}개의 할 일이 있어요!")
    
                for j, todo in enumerate(st.session_state.todolist[i]):
                    st.write(f"{j + 1}번째 할 일 : {todo}")
            else:
                st.info("아직 할 일이 없어요. ")
except:
    st.info("아직 아무도 없어요")
if st.button("전체 삭제"):
    st.session_state.todolist[st.session_state.Username.index(st.session_state.nowname)] = []
    st.info("모든 할 일이 삭제되었습니다")
    st.rerun()