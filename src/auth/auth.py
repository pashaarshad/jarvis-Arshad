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
    st.title("👤 Authentication Page")
    if st.button("Authenticate"):
      st.login("google")

  else:
    st.title("👤 Profile Page")
    st.image(st.user.picture, caption=st.user.name)
    st.write("Email:", st.user.email)
    st.write(f"Issued At: {unix_to_ist(st.user.iat)}")
    st.write(f"Expires At: {unix_to_ist(st.user.exp)}")
    if st.button("Log out"):
      st.logout()

auth()
