# Music Visualizer

A Python project that visualizes audio files by generating waveforms and spectrograms. This tool helps in analyzing audio signals by showing both time-domain (waveform) and frequency-domain (spectrogram) representations.

## Features

- Load and process audio files (supports MP3, WAV, and other common formats)
- Generate waveform visualization showing amplitude over time
- Create spectrograms displaying frequency content over time
- Simple and easy-to-use interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Surya-Raghuram/MusicVisualiser.git
cd MusicVisualiser
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your audio files in the `samples` directory

2. Run the main script to visualize both waveform and spectrogram:
```bash
python main.py
```

3. To visualize only the waveform:
```bash
python waveform.py
```

4. To visualize only the spectrogram:
```bash
python spectrogram.py
```

## Understanding the Visualizations

- **Waveform**: Shows how the amplitude of the audio signal changes over time
  - X-axis: Time (in seconds)
  - Y-axis: Amplitude

- **Spectrogram**: Shows how different frequencies in the audio signal change over time
  - X-axis: Time (in seconds)
  - Y-axis: Frequency (in Hz, logarithmic scale)
  - Color intensity: Amplitude of each frequency

## Project Structure

```
MusicVisualiser/
├── samples/           # Directory for audio files
├── audioLoader.py     # Audio file loading functionality
├── waveform.py        # Waveform visualization
├── spectrogram.py     # Spectrogram visualization
├── main.py           # Main script to run all visualizations
└── requirements.txt   # Project dependencies
```

## Adding Your Own Audio Files

1. Place your audio file (MP3, WAV, etc.) in the `samples` directory
2. Modify the file path in `main.py` or run the individual visualization scripts with your file:
```python
y, sr = audioLoader.loadAudio("samples/your_audio_file.mp3")
```

Feel free to submit issues and enhancement requests! 
