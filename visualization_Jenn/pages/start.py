import streamlit as st
# from dotenv import load_dotenv
# import os
# import pymysql
# import pandas as pd

# def load_df(user_smartstore, user_product_id):
#     # .env 파일 로드
#     load_dotenv()

#     # 환경 변수에서 MySQL 연결 정보 가져오기
#     db_host = os.getenv("DB_HOST")
#     db_user = os.getenv("DB_USER")
#     db_password = os.getenv("DB_PASSWORD")
#     db_name = os.getenv("DB_NAME")

#     # MySQL 연결 설정
#     conn = pymysql.connect(
#         host=db_host,        # MySQL 서버 주소
#         user=db_user,        # 사용자 이름
#         password=db_password,# 비밀번호
#         database=db_name,    # 데이터베이스 이름
#         charset="utf8mb4"    # 문자셋 설정
#     )

#     # 커서 생성
#     cursor = conn.cursor()

#     # SQL 쿼리 실행
#     query = f"SELECT * FROM reviews_p1 WHERE smartstore = %s AND product_id = %s;"
#     cursor.execute(query, (user_smartstore, user_product_id))

#     # 결과 가져오기
#     rows = cursor.fetchall()

#     # 컬럼 이름을 가져와서 DataFrame으로 변환
#     columns = [desc[0] for desc in cursor.description]
#     df = pd.DataFrame(rows, columns=columns)

#     # 연결 종료
#     cursor.close()
#     conn.close()

#     return df

# ###

st.title("네이버 쇼핑 ABSA 분석기")
st.write('내 상품에 대한 소비자 반응을 확인해보세요!')
if 'user_input_ss' not in st.session_state:
    st.session_state['user_input_ss'] = []

if 'user_input_p' not in st.session_state:
    st.session_state['user_input_p'] = []

with st.form("분석할 상품"):
    
    st.radio(
        "판매 루트 선택:",
        ["스마트스토어","브랜드관"]
    )

    user_smartstore = st.text_input('스토어 아이디')
    user_product_id = st.text_input('상품번호')

    submitted = st.form_submit_button("확인하기")
    if submitted:
        st.success("상품 분석을 시작했습니다. 분석 도구 탭을 확인해보세요!")
        st.session_state['user_input_ss'].append(user_smartstore)
        st.session_state['user_input_p'].append(user_product_id)

        # # st.write("loading reviews")
        # # 호출 시 store_id와 product_id를 전달하고 DataFrame 반환
        # df = load_df(user_smartstore, user_product_id)
        # st.write(df)  # DataFrame 출력
        # st.write("analyzing reviews")


st.subheader('검색 기록')

# 검색 기록 초기화 버튼
if st.button("검색 기록 초기화"):
    st.session_state['user_input_ss'] = []
    st.session_state['user_input_p'] = []
    st.success("검색 기록이 초기화되었습니다.")

with st.container(height=150):
    if st.session_state['user_input_ss'] and st.session_state['user_input_p']:
        for i, (ss_value, p_value) in enumerate(zip(st.session_state['user_input_ss'], st.session_state['user_input_p']), start=1):
            st.markdown(f"**[{i}] 스토어 아이디:** {ss_value}, **상품번호:** {p_value}")
    else:
        st.write("아직 검색 기록이 없습니다.")