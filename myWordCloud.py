# 분석 대상 문장 / 단어별 구분자 스페이스(공백 한칸)을 이용함
# 예시 문장 : 2019년 12월, 한국폴리텍대학 서울강서캠퍼스 데이터분석과 연합뉴스
text = "연합뉴스 한국폴리텍대학 서울강서캠퍼스(학장 조정희)는 데이터분석과 2학년 김한결, ..." \
       "훈련을 공공조직서 장려함을 받아 세종대학교에서 개최된 '소프트웨어(SW) 인재페스티벌'에 초청받았다고 10일 밝혔다." \
       "이번 수상한 작품은 빅데이터 분석을 활용한 AI 면접 스피치 교정 애플리케이션으로 최근 늘어나는 채용으로 인해..." \
       "면접에 대한 중요성이 강조되면서, 면접 교육을 위한 수요도 증가하고 있다." \
       "사용자는 텍스트, 스마트폰을 통한 음성 입력을 받아 마이크에 음성으로 면접 질문에 대해 대답하고, ..." \
       "소프트웨어는 그 데이터를 바탕으로 분석을 진행함. 특히, AI 내용은 자주 사용되는 명사 단어, 목소리의 높낮이, 목소리 빠르기, ..." \
       "긍/부정 단어 사용 여부 등이 분석, 음성인식(TTS), 오피니언 마이닝 등 기술이 적용됐다."

# 예시 문장 출력
print(text)

# 설치한 wordcloud 외부 라이브러리로부터 WordCloud 기능 사용하도록 설정
from wordcloud import WordCloud,STOPWORDS

# 설치한 matplotlib 외부 라이브러리의 pyplot 기능을 사용하여, pyplot 기능을 약어로 plt로 정의
import matplotlib.pyplot as plt

# stopwords 변수에 원하지 않는 단어들 추가
stopwords = set(STOPWORDS)
stopwords.add("위해")
stopwords.add("받아")
stopwords.add("분석을")

myWC = WordCloud(
    font_path="C:/Windows/Fonts/malgun.ttf",  # 또는 나눔고딕이 있다면 해당 경로
       stopwords=stopwords,
    background_color="white"
).generate(text)

# 워드 클라우드의 크기 정의
plt.figure(figsize=(5, 5))

# 워드 클라우드의 이미지의 부드럽기 정도
plt.imshow(myWC, interpolation="lanczos")

# x, y축에 기본 숫자들 제거
plt.axis("off")

# 워드 클라우드 보여주기
plt.show()

font_path="C:/Windows/Fonts/malgun.ttf"  # 또는 NanumGothic.ttf가 설치된 경로
