import streamlit as st
from dotenv import load_dotenv
import os
import pymysql
import pandas as pd

def load_df(user_smartstore, user_product_id):
    # .env 파일 로드
    load_dotenv()

    # 환경 변수에서 MySQL 연결 정보 가져오기
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    # MySQL 연결 설정
    conn = pymysql.connect(
        host=db_host,        # MySQL 서버 주소
        user=db_user,        # 사용자 이름
        password=db_password,# 비밀번호
        database=db_name,    # 데이터베이스 이름
        charset="utf8mb4"    # 문자셋 설정
    )

    # 커서 생성
    cursor = conn.cursor()

    # SQL 쿼리 실행
    query = f"SELECT * FROM reviews_p1 WHERE smartstore = %s AND product_id = %s;"
    cursor.execute(query, (user_smartstore, user_product_id))

    # 결과 가져오기
    rows = cursor.fetchall()

    # 컬럼 이름을 가져와서 DataFrame으로 변환
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    # 연결 종료
    cursor.close()
    conn.close()

    return df

###

st.title('대시보드')
st.write('내 상품에 대한 소비자 감성분석 결과를 확인해보세요!')

# session_state에서 가장 최근 값 읽기
if 'user_input_ss' in st.session_state and 'user_input_p' in st.session_state:
    ss_values = st.session_state['user_input_ss']
    p_values = st.session_state['user_input_p']

    if ss_values and p_values:
        # 가장 최근 입력값을 사용
        last_ss_value = ss_values[-1]  # 마지막 스토어 아이디
        last_p_value = p_values[-1]    # 마지막 상품번호
        
        # st.write(f"최근 검색 기록 - 스토어 아이디: {last_ss_value}, 상품번호: {last_p_value}")
        
        # 가장 최근 값에 대해 load_df 호출
        df = load_df(last_ss_value, last_p_value)
        st.write(df)  # DataFrame 출력
        
        # 분석 시작 표시
        # st.write("analyzing reviews")
    else:
        st.write("검색 기록이 없습니다.")
else:
    st.write("검색 기록이 없습니다.")
