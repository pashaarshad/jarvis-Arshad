from src.utils.functions import application
import streamlit as st

if __name__ == "__main__":
  if st.user and not st.user.is_logged_in:
    if st.button("Authenticate"):
      st.login("google")
  else:
    application().run()
