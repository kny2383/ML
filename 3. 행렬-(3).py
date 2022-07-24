#희소행렬을 직접 만들 때 사용하는 포맷
#COO포멧(Coordinate 포멧)
data = np.ones(4)

row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data,(row_indices,col_indices)))
print("COO 표현: \n{}".format(eye_coo))