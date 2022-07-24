#matplotlib: 과학계산용 그래프 라이브러리
#선 그래프, 히스토그램, 산점도 등 지원
#그래프를 그리기 위해서는 matplotlib의 pyplot 모듈을 이용

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label = "sin")
plt.plot(x,y2,linestyle= "--", label = "cos")
plt.title("sin/ cos grahp")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()