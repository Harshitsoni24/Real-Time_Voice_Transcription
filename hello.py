import streamlit as st
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        st.write("Transcribing...")
        text = r.recognize_google(audio)
        st.write("Transcription:", text)
    except sr.UnknownValueError:
        st.write("Could not understand audio.")
    except sr.RequestError as e:
        st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    st.title("Real-time Voice Transcription App")
    st.write("Click the 'Start Transcription' button and speak into your microphone.")

    if st.button("Start Transcription"):
        transcribe_audio()

if __name__ == "__main__":
    main()
