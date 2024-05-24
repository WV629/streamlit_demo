import streamlit as st

if 'is_login' not in st.session_state:
    st.session_state.is_login = False


@st.experimental_dialog("Register")
def vote():
    st.write(f"Register Your Account")
    user = st.text_input("请输入邮箱：")
    passwd = st.text_input("请输入您的密码：", type="password")
    re_passwd = st.text_input("请再次输入密码：", type="password")
    if st.button("Submit"):
        st.success("注册成功，您的账号为：" + user)


with st.sidebar:
    with st.container(border=True):
        st.text_input("请输入账号：")
        st.text_input("请输入密码：", type="password")
        left, right = st.columns(2)
        login = right.button("登录")
        register = left.button("注册")
        if register:
            vote()
        if login:
            st.session_state.is_login = True
            st.success("登录成功")
            session_id = ""


@st.experimental_fragment
def check_radio():
    if st.session_state.is_login:
        imgs = ["尸祖", "女帝", "李星云", "那谁"]
        st.snow()
        genre = st.radio(
            "what are you want see?",
            imgs
        )
        if genre:
            st.image("imgs/" + genre + ".png")


check_radio()
