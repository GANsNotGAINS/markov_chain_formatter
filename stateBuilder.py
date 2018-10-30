from numpy import array
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import numpy as np

class StateBuilder():
    def __init__(self, imgNameArr):
        if not isinstance(imgNameArr, list):
            imgNameArr = [imgNameArr]

        self.vector_int = dict()
        self.counter = 0

        for imgName in imgNameArr:
            self.createImgMarkovInput(imgName)

    def createImgMarkovInput(self, imgName):
        img = plt.imread(imgName)
        # row, col, channels = img.shape
        img = np.transpose(img, (1,0,2))
        markov_chain_input = list()

        for column in img:
            key = str(column)
            if key in self.vector_int:
               markov_chain_input.append(self.vector_int[key])
            else:
                self.vector_int[key] = self.counter
                markov_chain_input.append(self.counter)
                self.counter+=1

        return markov_chain_input