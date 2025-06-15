import matplotlib.pyplot as plt
import librosa
import librosa.display
import audioLoader

def plotWaveform(y,sr):
    """
    Plots the waveform of the input audio signal.
    Waveform shows how the amplitude of the audio signal changes over time.
    Args:
        y(nd.array): Audio samples.
        sr(int) : Sample rate.
    """
    plt.figure(figsize = (10,4))
    librosa.display.waveshow(y, sr = sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
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
    print("Plotting waveform...")
    try:
        plotWaveform(y,sr)
        print("Waveform plotted successfully!")
    except Exception as e:
        print(f"Error plotting waveform: {str(e)}")
        exit(1)
    
        