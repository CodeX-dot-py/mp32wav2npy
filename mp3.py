# first you need to download ffmpeg and extract it in your C directory
# then set an path environmental variable for ffmpeg Ex. 'C:/ffmpg/bin'
# modules to install 1.numpy, 2.scipy

# In this code I convert .mp3 files from one folder and store it in .wav in another folder

import os
import scipy.io.wavfile as wav
import numpy as np


def mass_song_converter():
    mp3_folder_path = ''  # path of the .mp3 folder
    wav_folder_path = ''  # path of the folder to be stored the wav format

    for name in os.listdir(mp3_folder_path):

        song_name, extension = name.split('.')
        mp3_path = os.path.join(mp3_folder_path, name)
        to_wav_path = wav_folder_path+song_name+'.wav'
        os.system('C:/ffmpeg/bin/ffmpeg.exe -i {} {}'.format(mp3_path, to_wav_path))


def single_song_converter():
    mp3_path = ''
    wav_path = ''

    os.system('C:/ffmpeg/bin/ffmpeg.exe -i {} {}'.format(mp3_path, wav_path))
    # C:/ffmpeg/bin/ffmpeg.exe this is the path location ffmpeg.exe


def wav_to_numpy_arr_converter():
    music_arr = []
    wav_path = ''

    for name in os.listdir(wav_path):
        frequency, wav_arr = wav.read(wav_path+'/'+name)
        music_arr.append(wav_arr)
        print(name, ' converted and append to numpy array')
    np.save('song_data.npy', music_arr)
