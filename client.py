#Importing Libraries

import os
import librosa
import librosa.display
import random
import pandas as pd
import numpy as np

#Ignoring depriciated warnings for test purposes
import warnings
warnings.filterwarnings('ignore')


def readData_Librosa(dataInfo):
    # List for Storing all the data
    Dataset = []

    try:
        audioData, audioSample_rate = librosa.load(dataInfo)
        Dataset.append(audioData)
        Dataset.append(audioSample_rate)

    except:
        print("Couldn't Find: ", dataInfo)

    return Dataset


# Reading data
Dataset = readData_Librosa("/Users/an0007/Desktop/ClientServer/Screenshot khencho.mp3")

print("Audio: ", Dataset[0])
print("\n\nShape: ", Dataset[0].shape)
print("\n\nsr: ", Dataset[1])


import socket
import sys

try:
    import cPickle as pickle
except ImportError:
    import pickle

sock = socket.socket()
data = Dataset[0]
sock.connect(('34.131.143.93',3389))
serialized_data = pickle.dumps(data, protocol=2)
sock.sendall(serialized_data)
sock.close()

import time
time.sleep(5)

sock = socket.socket()
sock.connect(('34.131.143.93',3389))
data = b''
while True:
    block = sock.recv(4096)
    if not block: break
    data += block

if sys.version_info.major < 3:
    unserialized_input = pickle.loads(data)
else:
    unserialized_input = pickle.loads(data, encoding='bytes')

print("Output from Server:", unserialized_input)

sock.close()