import streamlit as st
from datetime import datetime, date
from crawling import fortune_text

# 스타일 설정 함수
# def set_text_style():
#     style = """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#     html, body, [class*="st-"] {
#         font-family: 'Jua', sans-serif;
#         color: black;
#         background-color: #FFFFFF;
#     }

#     h1.title-box {
#         background-color: rgba(255, 255, 255, 0.6);
#         padding: 20px;
#         border-radius: 10px;
#         text-align: center;
#         color: black;
#     }

#     .block-container {
#         padding-top: 2rem;
#     }
#     </style>
#     """
#     st.markdown(style, unsafe_allow_html=True)


#################
# 초기 세션 상태
st.set_page_config(page_title="오늘의 운세", layout="wide")
today = datetime.now().strftime("%m월 %d일")
st.markdown(f"<h1 class='title-box'>{today} 오늘의 운세</h1>", unsafe_allow_html=True)


st.session_state.data = None
st.session_state.fortune = None

#################
# 사이드바 입력

st.sidebar.header("사용자 정보 입력")

gender = st.sidebar.radio("사용자 성별", ["남성", "여성"], horizontal=True)
if gender == "남성":
        sex ="M"
elif gender =="여성":
    sex = "F"

birth_date = st.sidebar.date_input("생년월일",
    value=date(2010, 1, 1),
    min_value=date(1930, 1, 1),
    max_value=datetime.today().date(),
    format="YYYY-MM-DD"
)

hour_lst = ["모름", "子(자) 23:30 ~ 01:29","丑(축) 01:30 ~ 03:29","寅(인) 03:30 ~ 05:29","卯(묘) 05:30 ~ 07:29","辰(진) 07:30 ~ 09:29","巳(사) 09:30 ~ 11:29","午(오) 11:30 ~ 13:29","未(미) 13:30 ~ 15:29","申(신) 15:30 ~ 17:29","酉(유) 17:30 ~ 19:29","戌(술) 19:30 ~ 21:29","亥(해) 21:30 ~ 23:29"]
birth_hour = st.sidebar.selectbox("출생시간", hour_lst)
for i, val in enumerate(hour_lst):
    if val == birth_hour:
        birth_i = i+1



#################
# 입력 버튼 실행

if st.sidebar.button("운세보기"):
    st.session_state.data = gender, birth_date.year, birth_date.month, birth_date.day, birth_hour
    st.session_state.fortune = fortune_text(sex, birth_date.year, birth_date.month, birth_date.day, birth_i)


#################
# 메인 페이지 출력

if st.session_state.fortune:
    data =st.session_state.fortune


# 운세 결과 출력

    st.subheader("오늘의 한줄 운세")
    st.info(data[0])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 총운")
        st.write(data[1])

        st.markdown("### 애정운")
        st.write(data[2])

    with col2:
        st.markdown("### 재물운")
        st.write(data[3])

        st.markdown("### 건강운")
        st.write(data[4])
