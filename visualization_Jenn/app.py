import streamlit as st


st.set_page_config(page_title="네이버 리뷰 ABSA 분석기", layout="centered", initial_sidebar_state="auto", menu_items=None)

# 홈 목록
start = st.Page("pages/start.py", title="시작하기", default=True)

# 영화 목록
test = st.Page("pages/test.py", title='summary')

pg = st.navigation(
    {
        "홈": [start],
        "분석 도구": [test],
    }
)
pg.run()

# st.sidebar.success("리뷰 분석 도구를 선택해주세요.")


