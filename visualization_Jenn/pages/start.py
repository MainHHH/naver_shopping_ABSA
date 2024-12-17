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

st.title("네이버 쇼핑 ABSA 분석기")

with st.form("분석할 상품"):
    user_smartstore = st.text_input('스토어 아이디')
    user_product_id = st.text_input('상품번호')

    submitted = st.form_submit_button("확인하기")
    if submitted:
        st.write("submitted")
        st.write("loading reviews")
        # 호출 시 store_id와 product_id를 전달하고 DataFrame 반환
        df = load_df(user_smartstore, user_product_id)
        st.write(df)  # DataFrame 출력
        st.write("analyzing reviews")
        