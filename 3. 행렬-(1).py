import numpy as np
#numpy에서 특수행렬을 만드는 함수
#eye(N,M=,k=,dtype)함수는 항등행렬을 생성하는 함수
#N은 행의 수, M은 열의 수, K는 대각의 위치

b1 = np.ones(10)
b2 = np.zeros((5,5))

b11 = np.ones((5,5))
np.eye(2, dtype = int)

np.eye(4, M=5, k=1, dtype = int)
np.eye(4, M=5, k=-1, dtype = int)

#diag()함수는 정방행렬에서 대각 요소만 추출하여 벡터를 만든다

x = np.arange(9).reshape(3,3)
print(x)
np.diag(x)
np.diag(x, k=1)
np.diag(x, k=-1)

np.diag(np.diag(x))