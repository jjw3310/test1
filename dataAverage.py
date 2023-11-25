import pandas as pd
import matplotlib.pyplot as plt

# Read csv file
data = pd.read_csv("TechChange.csv")

# 데이터 분석 예제: 기술 발전에 따른 시간별 평균 값 계산
# Data analysis example: Calculate the mean value by technology over time
mean_by_technology = data.groupby("technology")["output"].mean()

# 데이터 시각화: 기술별 시간별 평균 값 그래프
# Data analysis example: Calculate the mean value by technology over time
mean_by_technology.plot(kind="line", marker="o")
plt.xlabel("Technology")
plt.ylabel("Mean Output")
plt.title("Mean Output by Technology")
plt.grid(True)
plt.show()
