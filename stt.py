import speech_recognition as sr


def audio_to_text(audio_abs_path, IBM_USERNAME, IBM_PASSWORD):
    """
    Converts audio voice into written text using IBM Watson
    Parameters
    ----------
    audio_abs_path     str
    IBM_USERNAME       str
    IBM_PASSWORD       str
    Returns
    -------
    data          str
    """
    r = sr.Recognizer()

    with sr.AudioFile(audio_abs_path) as f:
        audio = r.record(f)

    data = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    return data
