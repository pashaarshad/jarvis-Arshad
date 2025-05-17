import streamlit as st
from datetime import datetime
import pytz

# Convert UNIX timestamps to IST
def unix_to_ist(timestamp):
  india_tz = pytz.timezone('Asia/Kolkata')
  format_str = '%I:%M:%S %p IST'
  return datetime.fromtimestamp(timestamp, pytz.utc).astimezone(india_tz).strftime(format_str)

def auth():
  if st.user and not st.user.is_logged_in:
    st.title("🔐 Login Required")
    st.write("Please authenticate using your Google account to access your profile.")
    if st.button("🔓 Authenticate with Google"):
      st.login("google")

  else:
    st.title(f"👤 Welcome, {st.user.given_name}")
    st.image(st.user.picture, caption=st.user.name)

    with st.expander("Login Credentials", expanded=True):
      st.write("Email:", st.user.email)
      st.write(f"Session logged in: {unix_to_ist(st.user.iat)}")
      st.write(f"Session expires at: {unix_to_ist(st.user.exp)}")

    if st.button("Log out"):
      st.logout()

auth()
