from scipy import sparse
import numpy as np
#scipy에서 scikit-learn 알고리즘을 구현할 때
#많이 사용하는 모듈은 scipy.sparse 모듈이다.
#희소 행렬(sparse metrix)

#정방행렬
b1 = np.eye(4, dtype=int)
print("Numpy 배열: \n{}.".format(b1))

#sparse.csr_matrix(): 0이 아닌 원소만 저장
sparse_matrix = sparse.csr_matrix(b1)
print("Scipy의 CSR 행렬: \n{}".format(sparse_matrix))

#CSR(Compressed Row Storage): 행의 인덱스를 압축해서 저장
b2 = np.eye(5, k=-1, dtype=int)
print(b2)

sparse_matrix = sparse.csr_matrix(b2)
print("Scipy의 CSR 행렬: \n{}".format(sparse_matrix))

b3 = np.arange(16).reshape(4,4)
print(b3)

y = np.diag(np.diag(b3))
print("----------------\n{}".format(y))

sparse_matrix = sparse.csr_matrix(y)
print("SCiPy의 CSR행렬: \n{}".format(sparse_matrix))