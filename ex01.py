import pandas as pd

print(pd.__version__)

# 판다스: 데이터 입출력, 탐색, 정제, 변환, 집계, 분석... 편하게 메서드
# Series 클래스
# DataFrame 클래스

# pandas.py
# class Series: 1차원 배열
# class DataFrame: 2차원 배열

s1 = pd.Series([1,3,5], index = [10, 20, 30]) #Sereis클래스의 생성자 함수
print(type(s1))
print(s1)