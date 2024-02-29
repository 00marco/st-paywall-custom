import streamlit as st
from st_paywall import add_auth




st.set_page_config(layout="wide")
st.title("🎈 Tyler's Subscription app POC 🎈")

st.session_state.user_subscribed = False

def callback_test():
    st.toast("Callback worked!")

add_auth(
    required=False,
    login_button_text="Login with Google",
    login_button_color="#FD504D",
    login_sidebar=False,
    subscribe_now_sidebar=False,
    on_login=callback_test
)

if st.session_state.user_subscribed:
    st.write("Congrats, you are subscribed!")
    st.write("the email of the user is " + str(st.session_state.email))
