import string



class TextCleaner:

    @staticmethod
    def clean_text(text):
        clean_text = text.translate(str.maketrans('', '', string.punctuation))
        upp_text = clean_text.upper()
        return upp_text