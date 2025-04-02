import streamlit as st
from datetime import datetime, date
import 운세_모듈

# 스타일 설정 함수
def set_text_style():
    style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Jua', sans-serif;
        color: white;
        background-color: #222222;
    }

    h1.title-box {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# 페이지 설정
st.set_page_config(page_title="오늘의 운세", layout="wide")
set_text_style()

# 세션 상태
if "운세보기" not in st.session_state:
    st.session_state["운세보기"] = False

# 오늘 날짜 제목
today = datetime.now().strftime("%m월 %d일")
st.markdown(f"<h1 class='title-box'>{today} 오늘의 운세</h1>", unsafe_allow_html=True)

# 사용자 입력 - 사이드바
with st.sidebar:
    st.header("사용자 정보 입력")
    gender = st.radio("사용자 성별", ["남성", "여성"], horizontal=True)

    birth_date = st.date_input(
        "생년월일",
        value=date(2010, 1, 1),
        min_value=date(1930, 1, 1),
        max_value=datetime.today().date(),
        format="YYYY-MM-DD"
    )

    birth_hour = st.selectbox("출생시간", ["모름"] + [f"{h}시" for h in range(24)])

    if st.button("운세보기"):
        st.session_state["운세보기"] = True
        st.rerun()

# 운세 결과 출력
if st.session_state["운세보기"]:
    st.subheader("오늘의 한줄 운세")
    st.info(운세_모듈.get_한줄운세())

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 총운")
        st.write(운세_모듈.get_총운())

        st.markdown("### 애정운")
        st.write(운세_모듈.get_애정운())

    with col2:
        st.markdown("### 재물운")
        st.write(운세_모듈.get_재물운())

        st.markdown("### 건강운")
        st.write(운세_모듈.get_건강운())

else:
    st.info("왼쪽에서 정보를 입력하고 '운세보기' 버튼을 눌러주세요.")

