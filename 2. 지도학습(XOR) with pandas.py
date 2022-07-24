import pandas as pd
from sklearn import svm, metrics

#XOR 연산 데이터
inputData = [[0,0,0],
            [0,1,1],
            [1,0,1],
            [1,1,0]
]

xor_df = pd.DataFrame(inputData) # 1차원 : Series(), 2차원: DataFrame

#학습데이터와 레이블을 분리
trainingData = xor_df.loc[:,0:1] # column의 인덱스를 0~1까지(범위: 끝 index를 포함)
label = xor_df.loc[:,2] # 1차원

#머신 러닝 객체 만들기
clf = svm.SVC()
#데이터의 학습과 예측
clf.fit(trainingData, label)
#print(trainingData, label)
pre = clf.predict(trainingData)

#정확도 측정(정답률 확인)
#metrics 모듈에 accuracy_score(label, pre)
 
accuracy = metrics.accuracy_score(label, pre) #성공율을 구하는 함수
print("정확도", accuracy)