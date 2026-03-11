import speech_recognition as sr



class SpeachToText:

    def __init__(self):
        self.r = sr.Recognizer()


    def wav_file_to_text(self, audio_path: str):
        audio = sr.AudioData.from_file(audio_path)

        try:
            return self.r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service. \nDetails: {e}"