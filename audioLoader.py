import librosa

def loadAudio(audioPath):
    """
    Loads an audio file and returns the audio data and sample rate.
    Args:
        audioPath (str): The path to the audio file.
    Returns:
        y (np.ndarray): The audio data.
        sr (int): The sample rate.
    """
    y,sr = librosa.load(audioPath, duration = 30)
    return y,sr

if __name__ == "__main__":
    print("Attempting to load audio file...")
    try:
        y, sr = loadAudio("samples/sample1.mp3")
        print(f"Sample rate: {sr} Hz")
        print(f"Audio shape: {y.shape}")
        print(f"First few samples: {y[:5]}")
    except Exception as e:
        print(f"Error loading audio: {str(e)}")