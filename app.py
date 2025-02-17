import streamlit as st

ALLOWED_USERS = st.secrets["auth"]["allowed_users"]

if not st.experimental_user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.experimental_user.email in ALLOWED_USERS:
        st.write("인증된 사용자입니다.")
    else:
        st.write("인증이 필요합니다. 관리자에게 요청하세요.")
    st.write(f"Hello, {st.experimental_user.name}!")
    st.write(st.experimental_user)
    if st.button("Log out"):
        st.logout()
