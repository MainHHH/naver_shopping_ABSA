import streamlit as st


st.set_page_config(page_title="네이버 리뷰 ABSA 분석기", layout="centered", initial_sidebar_state="auto", menu_items=None)

# 홈 목록
start = st.Page("pages/start.py", title="시작하기", default=True)

# 분석 도구 목록
dashboard = st.Page("pages/dashboard.py", title='대시보드')

pg = st.navigation(
    {
        "홈": [start],
        "분석 도구": [dashboard],
    }
)
pg.run()


