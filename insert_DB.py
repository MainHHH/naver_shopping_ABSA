import pymysql
import os
import pandas as pd
import sys
from dotenv import load_dotenv


def insert_db(csv):
    data = pd.read_csv(csv)

    load_dotenv()

    # 데이터베이스 연결
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        charset="utf8mb4",
    )

    try:
        with connection.cursor() as cursor:
            filtered_data = []
            for _, row in data.iterrows():
                check_sql = """
                    SELECT 1
                    FROM reviews
                    WHERE product_id = %s
                      AND product_option = %s
                      AND user_id = %s
                      AND apply_date = %s
                """
                cursor.execute(check_sql, (row['product_id'], row['product_option'], row['user_id'], row['apply_date']))
                if not cursor.fetchone():
                    filtered_data.append(
                        (
                            row['smartstore'], row['product_name'], row['product_id'], row['product_option'], row['user_id'], row['apply_date'], row['review'], row['stars_score'], row['thumb_count']
                        )
                    )

            if filtered_data:
                print("inserting...")
                insert_sql = """
                INSERT INTO reviews (smartstore, product_name, product_id, product_option, user_id, apply_date, review, stars_score, thumb_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.executemany(insert_sql, filtered_data)

            connection.commit()
    finally:
        print("done")
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        insert_db(argument)
    else:
        print("No argument provided.")