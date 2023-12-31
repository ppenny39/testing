import streamlit as st

def main():
    
    st.title("맥주 추천 앱")

    # 사용자 입력값 받기
    도수 = st.selectbox("도수", ["낮음", "보통", "높음"])
    맥아 = st.selectbox("맥아", ["보리", "밀", "라이"])
    효모 = st.selectbox("효모", ["에일", "라거", "스타우트", "크래프트"])
    칼로리 = st.selectbox("칼로리", ["낮음", "보통", "높음"])
    홉 = st.selectbox("홉", ["쓴맛", "깔끔한 맛", "고소한 맛", "상쾌한 맛", "고급스러운 맛", "풍미로운 맛", "시원한 맛"])
    생산지 = st.selectbox("생산지", ["한국", "미국", "독일", "폴란드", "벨기에", "일본", "네덜란드"])

    
if __name__ == "__main__":
    main()