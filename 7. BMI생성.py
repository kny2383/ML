import random

#BMI 계산 함수
def bmi_func(height,weight):
    bmi = weight/(height/100)**2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "nomal"
    return "fat"

#출력 파일 준비
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

#랜덤 데이터 생성
cnt = {"thin":0, "nomal":0, "fat":0}

for i in range(10000):
    h = random.randint(120,200)
    w = random.randint(35,90)
    label = bmi_func(h,w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))
fp.close()
print("OK",cnt)