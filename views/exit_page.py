"""Menu 9 - Exit."""

import streamlit as st


def page_exit():
    st.header("Exit")
    st.success("Thank you for using Smart Bus Reservation System!")
    st.write("You can now close this browser tab. "
             "Remember: all data is kept in memory only and will be "
             "lost when the app is closed or restarted.")
