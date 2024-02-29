import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os 
from loguru import logger

fs = 44100  # Sample rate
duration = 10  # Duration of recording in seconds

folder_path = 'audiofiles'



def main():
    filename = input("Enter the filename for the recording (without extension): ") + '.wav'
    logger.info("Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    logger.info("Recording stopped") 

    file_path = os.path.join(folder_path, f'{filename}')
        
    # Save recording as a WAV file
    wav.write(file_path, fs, myrecording)