from numpy import array
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import numpy as np
# create dense matrix
img = plt.imread('test.png')
row, col, channels = img.shape
img = np.transpose(img, [1,0,2])

print(img.shape)


vector_int = dict()
markov_chain_input = list()
counter=0
#convert to sparse matrix, then place into a dict
for column in img:
    key = str(column)
    #print(key)
    if key in vector_int:
       markov_chain_input.append(vector_int[key])
    else:
        vector_int[key] = counter
        markov_chain_input.append(counter)
        counter+=1

#print(vector_int)
print(len(markov_chain_input))




#print(B)