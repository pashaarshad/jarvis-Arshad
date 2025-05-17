from datetime import datetime
import streamlit as st

today = datetime.now()

# /auth
auth_page = st.Page("src/auth/auth.py", title="Authentication", icon=":material/lock_open:")

# /apps/public
home = st.Page("src/apps/public/home.py", title="Home", icon=":material/home:")
youtubePlaylist = st.Page("src/apps/public/youtubePlaylist.py", title="Jarvis Videos", icon=":material/ondemand_video:")

# /apps/pages/automations
coding = st.Page("src/apps/pages/automations/coding.py", title="Coding Platforms", icon=":material/code:")
websites = st.Page("src/apps/pages/automations/website.py", title="Websites", icon=":material/web:")
socialMediaApps = st.Page("src/apps/pages/automations/socialMediaApps.py", title="Social Media Apps", icon=":material/share:")
messenger = st.Page("src/apps/pages/automations/messenger.py", title="Messenger", icon=":material/email:")

# /apps/pages/models
chatBotModels = st.Page("src/apps/pages/models/chatBotModel.py", title="Chat Bot Models", icon=":material/smart_toy:")
healthCareModels = st.Page("src/apps/pages/models/healthCareModel.py", title="Health Care Models", icon=":material/health_and_safety:")
objectDetectionModels = st.Page("src/apps/pages/models/objectDetectionModel.py", title="Object Detection Models", icon=":material/camera_alt:")
recommendationModels = st.Page("src/apps/pages/models/recommendationModel.py", title="Recommendation Models", icon=":material/recommend:")

# /apps/pages/programs
simplePrograms = st.Page("src/apps/pages/programs/simpleProgram.py", title="Simple Programs", icon=":material/emoji_objects:")
apiPrograms = st.Page("src/apps/pages/programs/apiProgram.py", title="API Programs", icon=":material/api:")
imagePrograms = st.Page("src/apps/pages/programs/imageProgram.py", title="Image Programs", icon=":material/image:")
games = st.Page("src/apps/pages/programs/games.py",title="Games",icon=":material/casino:")
studyPrograms = st.Page("src/apps/pages/programs/studyProgram.py", title="Study Programs", icon=":material/school:")

def application():
  if st.user and not st.user.is_logged_in:
    pages = {
      "": [home, youtubePlaylist],
      "Account": [auth_page],
      "Automations": [coding, websites, socialMediaApps, messenger],
      "Models": [chatBotModels, healthCareModels, objectDetectionModels, recommendationModels],
      "Programs": [apiPrograms, games, imagePrograms, simplePrograms, studyPrograms],
    }

  return st.navigation({"": [home, youtubePlaylist], "Account": [auth_page]})
