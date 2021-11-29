import numpy as np
import librosa
import os
from update_library import refresh_library
from fastdtw import fastdtw
from pathlib2 import Path


def dist_func(x, y):
    return np.linalg.norm(x - y, ord=1)


def predict(song_dir):
    y, sr = librosa.load(song_dir, mono=True)
    _, beats = librosa.beat.beat_track(y, sr)
    x = np.array(librosa.feature.delta(beats)).reshape(-1, 1)
    distances = {}
    for song in library.keys():
        y = np.array(library[song]).reshape(-1, 1)
        dist = fastdtw(x, y, dist=dist_func)
        distances[song] = dist
    return min(distances, key=distances.get)


def test_single():
    filename = input("Enter file path: ")
    prediction = predict(filename)
    correct = prediction == Path(filename).stem
    print("Input: ", filename, " Prediction: ", prediction, " Correct:", correct)


def test_multi():
    test_dir = input("Enter test directory: ")
    valid_tests = 0
    correct_predictions = 0
    tests = os.listdir(test_dir)
    for test in tests:
        if test.endswith('.wav'):
            valid_tests += 1
            expected_label = Path(test).stem
            prediction = predict(os.path.join(test_dir, test))
            correct = expected_label == prediction
            if correct:
                correct_predictions += 1
            print("Input: ", expected_label, " Prediction: ", prediction, " Correct:", correct)
    print("Accuracy: ", 100.0 * float(correct_predictions / valid_tests), " %")


def main():
    refresh_library("source")
    mode = input("Test mode (one - returns prediction / multi - returns accuracy): ")
    global library
    library = np.load('lib.npy', allow_pickle=True).item()
    if mode == "one":
        test_single()
    elif mode == "multi":
        test_multi()


if __name__ == '__main__':
    main()
