from sklearn import svm

#1. 데이터 준비

xor_data = [[0,0,0],
            [0,1,1],
            [1,0,1],
            [1,1,0]
]

# 주어진 데이터를 분리(학습데이터와 정답레이블)
training_data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    res = row[2]
    
    training_data.append([p,q])
    label.append(res)

#2. 모델 표현 방법
# SVM알고리즘을 사용하는 머신러닝 객체를 만든다.
clf = svm.SVC() #서포트벡터머신 객체 생성

# fit() 메서드 : 학습기계에 데이터를 학습시킨다.
clf.fit(training_data, label) # 기계학습

#3. 모델 평가
# predict() 메서드 : 학습데이터를 이용하여 예측한다.
pre = clf.predict(training_data)
print("예측결과 :", pre)

ok = 0; total = 0

for idx, answer in enumerate(label): 
    p = pre[idx]
    if p == answer: 
        ok += 1
        total += 1
print("정확도: ", ok, "/", total, "=", ok/total)