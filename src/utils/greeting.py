from datetime import datetime

def GreetUser(name):
  hour = datetime.now().hour
  if 5 <= hour < 11:
    return f"Good Morning, {name}"
  elif 11 <= hour < 17:
    return f"Good Afternoon, {name}"
  elif 17 <= hour < 21:
    return f"Good Evening, {name}"
  return f"Good Night, {name}"
