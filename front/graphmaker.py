import matplotlib.pyplot as plt

# 예시 데이터
carbon_metro_M = 0.123
carbon_metro_m = 0.136

# 변수 이름과 값 리스트
labels = ['carbon_metro_M', 'carbon_metro_m']
values = [carbon_metro_M, carbon_metro_m]

# 막대 그래프 그리기
plt.bar(labels, values, color=['skyblue', 'orange'])

# 제목 및 축 이름 설정
plt.title('Carbon Emission Comparison')
plt.ylabel('Value')

# 값 표시하기 (막대 위에 숫자)
for i, v in enumerate(values):
    plt.text(i, v + 0.005, f"{v:.3f}", ha='center')

# 그래프를 파일로 저장
plt.savefig('carbon_bar_chart.png')

# 그래프 보여주기
plt.show()
