from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 분석할 문장
text = """
2019년 12월, 한국폴리텍대학 서울강서캠퍼스 데이터분석과 2학년 김한결, 홍유영, 홍두표 학생과 1학년 김도우 학생이
소프트웨어 인재페스티벌에 초청되었다. 이들은 AI 기반 면접 분석 프로그램을 개발하였다.
"""

# 1. Okt 형태소 분석기 객체 생성
okt = Okt()

# 2. 명사만 추출
nouns = okt.nouns(text)

# 3. 단어들을 공백 기준으로 연결
joined_text = ' '.join(nouns)

# 4. 워드클라우드 생성
wc = WordCloud(
    font_path="C:/Windows/Fonts/malgun.ttf",  # 또는 NanumGothic.ttf (윈도우 한글 폰트)
    background_color='white',
    width=800,
    height=600
).generate(joined_text)

# 5. 출력
plt.figure(figsize=(10, 8))
plt.imshow(wc, interpolation='lanczos')
plt.axis('off')
plt.show()
