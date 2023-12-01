import streamlit as st

# 사용자로부터 입력을 받는 스트림릿 애플리케이션을 생성합니다.
st.title('맥주 추천 앱')

# 사용자로부터 입력을 받는 부분
st.header('맛 프로필 입력')
bitterness = st.slider('쓴맛 (Bitterness)', 0, 10, 5)
sweetness = st.slider('단맛 (Sweetness)', 0, 10, 5)
alcohol = st.slider('알콜 함량 (Alcohol Content)', 0, 100, 5)
def recommend_beer(bitterness, sweetness, alcohol):
    # 간단한 추천 로직을 여기에 구현
    # 예: 쓴맛, 단맛, 알콜 함량 등을 고려하여 맥주 추천
    return "추천 맥주: 아주 좋은 맥주"

# 사용자 입력을 기반으로 맥주 추천
if st.button('맥주 추천'):
    recommended_beer = recommend_beer(bitterness, sweetness, alcohol)
    st.subheader('추천 맥주')
    st.write(recommended_beer)
