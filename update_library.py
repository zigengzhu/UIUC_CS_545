import numpy as np
import librosa
import os
from pydub import AudioSegment
from pathlib2 import Path


def reformat_all(source_dir):
    music_list = os.listdir(source_dir)
    for song in music_list:
        if song.endswith('.mp3'):
            song_wav = Path(song).stem + '.wav'
            if song_wav not in music_list:
                song_path = os.path.join(source_dir, song)
                output_path = os.path.join(source_dir, song_wav)
                AudioSegment.from_mp3(song_path).export(output_path, format="wav")
                print("Converted ", song, " to ", song_wav)


def create_library(source_dir):
    reformat_all(source_dir)
    music_list = os.listdir(source_dir)
    library = {}
    for song in music_list:
        if song.endswith('.wav'):
            song_dir = os.path.join(source_dir, song)
            y, sr = librosa.load(song_dir, mono=True)
            _, beats = librosa.beat.beat_track(y, sr)
            library[Path(song).stem] = librosa.feature.delta(beats)
            print('Added ', song, ' to library')
    np.save('lib.npy', library)


def refresh_library(source_dir):
    library = np.load('lib.npy', allow_pickle=True).item()
    reformat_all(source_dir)
    music_list = os.listdir(source_dir)
    for song in music_list:
        if song.endswith('.wav') and Path(song).stem not in library.keys():
            song_dir = os.path.join(source_dir, song)
            y, sr = librosa.load(song_dir, mono=True)
            _, beats = librosa.beat.beat_track(y, sr)
            library[Path(song).stem] = librosa.feature.delta(beats)
            print('Added ', song, ' to library')
    np.save('lib.npy', library)


def main():
    if 'lib.npy' not in os.listdir(os.curdir):
        create_library('source')
    else:
        refresh_library('source')


if __name__ == '__main__':
    main()




