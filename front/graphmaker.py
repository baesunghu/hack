import matplotlib.pyplot as plt

# ���� ������
carbon_metro_M = 0.123
carbon_metro_m = 0.136

# ���� �̸��� �� ����Ʈ
labels = ['carbon_metro_M', 'carbon_metro_m']
values = [carbon_metro_M, carbon_metro_m]

# ���� �׷��� �׸���
plt.bar(labels, values, color=['skyblue', 'orange'])

# ���� �� �� �̸� ����
plt.title('Carbon Emission Comparison')
plt.ylabel('Value')

# �� ǥ���ϱ� (���� ���� ����)
for i, v in enumerate(values):
    plt.text(i, v + 0.005, f"{v:.3f}", ha='center')

# �׷����� ���Ϸ� ����
plt.savefig('carbon_bar_chart.png')

# �׷��� �����ֱ�
plt.show()
