import win32com.client

def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

text1 = "Hello, My Name is Ali Muhammad"
text2 = "I am a Website Developer"
text3 = "I am a Computer Science Student"
speak(text1)
speak(text2)
speak(text3)

