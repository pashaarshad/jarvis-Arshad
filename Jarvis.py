import streamlit as st

# /auth
auth_page = st.Page("src/auth/auth.py", title="Authentication", icon=":material/lock_open:")

# /apps/public
home = st.Page("src/apps/public/home.py", title="Home", icon=":material/home:")
youtubePlaylist = st.Page("src/apps/public/youtubePlaylist.py", title="Jarvis Videos", icon=":material/ondemand_video:")

MAIN_DIR = 'src/apps/pages'

# /automations
coding = st.Page(f"{MAIN_DIR}/automations/coding.py", title="Coding Platforms", icon=":material/code:")
websites = st.Page(f"{MAIN_DIR}/automations/website.py", title="Websites", icon=":material/web:")
socialMediaApps = st.Page(f"{MAIN_DIR}/automations/socialMediaApps.py", title="Social Media Apps", icon=":material/share:")
messenger = st.Page(f"{MAIN_DIR}/automations/messenger.py", title="Messenger", icon=":material/email:")

# /models
chatBotModels = st.Page(f"{MAIN_DIR}/models/chatBotModel.py", title="Chat Bot Models", icon=":material/smart_toy:")
healthCareModels = st.Page(f"{MAIN_DIR}/models/healthCareModel.py", title="Health Care Models", icon=":material/health_and_safety:")
objectDetectionModels = st.Page(f"{MAIN_DIR}/models/objectDetectionModel.py", title="Object Detection Models", icon=":material/camera_alt:")
recommendationModels = st.Page(f"{MAIN_DIR}/models/recommendationModel.py", title="Recommendation Models", icon=":material/recommend:")

# /programs
simplePrograms = st.Page(f"{MAIN_DIR}/programs/simpleProgram.py", title="Simple Programs", icon=":material/emoji_objects:")
apiPrograms = st.Page(f"{MAIN_DIR}/programs/apiProgram.py", title="API Programs", icon=":material/api:")
imagePrograms = st.Page(f"{MAIN_DIR}/programs/imageProgram.py", title="Image Programs", icon=":material/image:")
games = st.Page(f"{MAIN_DIR}/programs/games.py",title="Games",icon=":material/casino:")
studyPrograms = st.Page(f"{MAIN_DIR}/programs/studyProgram.py", title="Study Programs", icon=":material/school:")

def application():
  pages = {
    "": [home, youtubePlaylist],
    "Account": [auth_page],
  }

  if st.user and st.user.is_logged_in:
    pages.update({
      "Automations": [coding, websites, socialMediaApps, messenger],
      "Models": [chatBotModels, healthCareModels, objectDetectionModels, recommendationModels],
      "Programs": [apiPrograms, games, imagePrograms, simplePrograms, studyPrograms],
    })

  return st.navigation(pages)

application().run()
