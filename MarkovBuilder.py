import numpy as np
import pickle
import vomm
from StateBuilder import StateBuilder
from scipy.misc import imsave

class MarkovBuilder():
    def __init__(self, imgNameArr, order=2):
        if not isinstance(imgNameArr, list):
            imgNameArr = [imgNameArr]

        stateBuilder = StateBuilder(imgNameArr)
        self.stateIntMap = stateBuilder.vector_int
        alphabet_size = len(self.stateIntMap)

        self.model = vomm.ppm()

        self.model.fit(np.array(stateBuilder.convertedSongs).flatten(), d=order, alphabet_size=alphabet_size)


        self.inverseMap = {v: k for k, v in self.stateIntMap.items()}
        # [i for i in range(len(self.stateIntMap))]

    def generateRandomSong(self, songName, songLength=100):
        # todo, count # beats in song, end after `songLength` but when
        # num beats are subdivisible by 4
        unmappedSong = self.model.generate_data(length=songLength)
        img = np.array([np.array(pickle.loads(self.inverseMap[stateNum])) for stateNum in unmappedSong])
        print(img.shape)
        img = np.transpose(img, (1, 0, 2))
        imsave(songName, img)

if __name__ == '__main__':
    mb = MarkovBuilder('mega.png', order=4)
    mb.generateRandomSong('megaRandom.png', songLength=300)


# training_data = [ord(x) - 97 for x in "abababab" ]

# my_model  = vomm.ppm()
# my_model.fit(training_data, d=2, alphabet_size=2)
# data = my_model.generate_data(length=300)
# print(''.join([chr(x+97) for x in data]))
# print(my_model)