import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("hello i am jarvis how can i help you")
    s = input()
    speaker.speak(s)