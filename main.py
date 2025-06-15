import audioLoader
import waveform
import spectrogram

path = "samples/sample1.mp3"

if __name__ == "__main__":
    print("Loading audio file...")
    try:
        y, sr = audioLoader.loadAudio(path)
        print("Audio loaded successfully!")
    except Exception as e:
        print(f"Error loading audio: {str(e)}")
        exit(1)
    print("Plotting waveform...")
    try:
        waveform.plotWaveform(y,sr)
        print("Waveform plotted successfully!")
    except Exception as e:
        print(f"Error plotting waveform: {str(e)}")
        exit(1)
    print("Plotting spectrogram...")
    try:
        spectrogram.plotSpectrogram(y,sr)
        print("Spectrogram plotted successfully!")
    except Exception as e:
        print(f"Error plotting spectrogram: {str(e)}")
        exit(1) 