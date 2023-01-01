# https://salu133445.github.io/lakh-pianoroll-dataset/
import os
import numpy as np
import pypianoroll
import matplotlib.pyplot as plt

# hack around use of np.int used in pretty_midi.py line 295
# numpy.int was removed from numpy at some point
np.int = int
multitrack = pypianoroll.read('./Billy_Joel_-_Allentown.mid')
print(multitrack)
multitrack.plot()
plt.show()

for npz_file in os.listdir('./'):
    if npz_file[-4:] != '.npz':
        continue
    data = np.load(npz_file)
    lst = data.files
    for item in lst:
        print(item)
        print(data[item])
