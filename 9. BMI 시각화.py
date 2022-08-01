import pandas as pd
import matplotlib.pyplot as plt

tb1 = pd.read_csv("bmi.csv", index_col = 2)

fig = plt.figure() # 판 가져오기
ax = fig.add_subplot(1,1,1)

def scatter(lbl, color):
    b = tb1.loc[lbl]
    ax.scatter(b["weight"],b["height"], c=color, label=lbl)
scatter("fat", "red")
scatter("nomal", "yellow")
scatter("thin", "purple")

ax.legend()
plt.savefig("bmi-test.png")