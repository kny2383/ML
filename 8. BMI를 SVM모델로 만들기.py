from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

#1. 데이터 읽어오기
tb1 = pd.read_csv("bmi.csv") # DataFrame

#컬럼 자르고 정규화하기
label = tb1["label"]
w = tb1["weight"]
h = tb1["height"]
wh = pd.concat([w,h], axis = 1) # DataFrame을 합치는 메서드

#학습 전용 데이터와 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = \
train_test_split(wh, label)

#2. 모델표현 방법: 알고리즘 -> SVM
#데이터 학습하기
clf = svm.SVC()
clf.fit(data_train, label_train) #기계학습: 머신러닝의 모델 생성

#3. 모델 평가
#데이터 예측하기
predict = clf.predict(data_test)
 
#결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("정답률 = ", ac_score)
print("리포트 = \n", cl_report)