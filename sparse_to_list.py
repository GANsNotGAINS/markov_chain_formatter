from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([[1, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])

S = csr_matrix(A)
print(S.indices)
print(S.indptr)


vector_int = dict()
markov_chain_input = list()
counter=0
#convert to sparse matrix, then place into a dict
for column in A.T:
    sparse = csr_matrix(column)
    key = tuple(sparse.indices)
    if key in vector_int:
       markov_chain_input.append(vector_int[key])
    else:
        vector_int[key] = counter
        markov_chain_input.append(counter)
        counter+=1
print(vector_int)
print(markov_chain_input)




#print(B)