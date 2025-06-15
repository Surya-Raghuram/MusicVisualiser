import librosa
import librosa.display
import audioLoader
import matplotlib.pyplot as plt
import numpy as np

def plotSpectrogram(y,sr):
    """
    Plots the spectrogram of the input audio signal.
    Spectrogram shows how the amplitude of different frequencies change over time.
    Args:
        y(nd.array): Audio samples.
        sr(int) : Sample rate.
    """
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)),ref = np.max)
    plt.figure(figsize = (10,4))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='magma')
    plt.title("Spectrogram")
    plt.colorbar(format="%+2.0f dB")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Loading audio file...")
    try:
        y, sr = audioLoader.loadAudio("samples/sample1.mp3")
        print("Audio loaded successfully!")
        print(f"Sample rate: {sr} Hz")
        print(f"Audio shape: {y.shape}")
        print(f"First few samples: {y[:5]}")
    except Exception as e:
        print(f"Error loading audio: {str(e)}")
        exit(1)
    print("Plotting spectrogram...")
    try:
        plotSpectrogram(y,sr)
        print("Spectrogram plotted successfully!")
    except Exception as e:
        print(f"Error plotting spectrogram: {str(e)}")
        exit(1)