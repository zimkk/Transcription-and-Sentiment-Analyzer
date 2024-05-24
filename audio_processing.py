import nltk
import speech_recognition as sr

import os

def convert_audio_to_text(filename=None):
    """
    Convert audio to text using Google Speech Recognition API.

    Args:
        filename (str): Path to the audio file.

    Returns:
        str: Recognized text formatted into sentences.
    """
    try:
        import speech_recognition as sr
    except ImportError:
        print("Error: speech_recognition module not found. Please install it using 'pip install SpeechRecognition'.")
        return ""

    r = sr.Recognizer()
    if filename:  # Check if filename argument is provided
        audio_path = os.path.join("audio", filename)  # Assuming audio files are in a folder named "audio"
        if not os.path.exists(audio_path):
            print(f"Error: File '{filename}' not found in the 'audio' folder.")
            return ""
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
    else:
        # Prompt user to speak into the microphone
        try:
            with sr.Microphone() as source:
                print("Please start speaking...")
                audio = r.listen(source)
        except sr.RequestError as e:
            print("Error: Couldn't access microphone; {0}".format(e))
            return ""
        except sr.UnknownValueError:
            print("Error: Unknown value received from microphone.")
            return ""
