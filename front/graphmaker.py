import matplotlib.pyplot as plt
import matplotlib
import os
import matplotlib.font_manager as fm
matplotlib.use('Agg')


def graphmaker(v1, v2):
    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_name = fm.FontProperties(fname=font_path).get_name()

    plt.rc('font', family=font_name)
    # 예시 데이터
    carbon_car = v1
    carbon_metro_avg = v2

    labels = ['자동차의 탄소 배출량', '지하철의 탄소 배출량']
    values = [carbon_car, carbon_metro_avg]

    plt.bar(labels, values, color=['skyblue', 'orange'])
    plt.title('탄소 배출량 분석')
    plt.ylabel('탄소 배출량')

    for i, v in enumerate(values):
        plt.text(i, v + 0.005, f"{v:.3f}", ha='center')

    # 현재 파이썬 파일이 실행된 디렉토리 위치 구하기
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 저장할 파일 경로 만들기
    save_path = os.path.join(current_dir, 'static/images/carbon_bar_chart.png')

    plt.savefig(save_path)
    plt.close()
