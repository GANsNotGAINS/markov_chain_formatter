from numpy import array
from scipy.misc import imread
import numpy as np
import pickle

class StateBuilder():
    def __init__(self, imgNameArr):
        if not isinstance(imgNameArr, list):
            imgNameArr = [imgNameArr]

        self.vector_int = dict()
        self.counter = 0
        self.convertedSongs = []

        for imgName in imgNameArr:
            convertedSong = self.createImgMarkovInput(imgName)
            self.convertedSongs.append(convertedSong)

    def createImgMarkovInput(self, imgName):
        img = imread(imgName)
        # row, col, channels = img.shape
        img = np.transpose(img, (1,0,2))

        markov_chain_input = list()

        for column in img:
            key = pickle.dumps(column, protocol=0)
            if key in self.vector_int:
               markov_chain_input.append(self.vector_int[key])
            else:
                self.vector_int[key] = self.counter
                markov_chain_input.append(self.counter)
                self.counter+=1

        return markov_chain_input