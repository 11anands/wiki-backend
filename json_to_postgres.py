import json
from app.config import settings
import psycopg2

with psycopg2.connect(dbname=settings.DB_NAME, user=settings.DB_USER, password=settings.DB_PASSWORD, port=settings.DB_PORT) as conn:
    with conn.cursor() as cur:
        with open("constants/drugs.json") as my_file:
            data = json.load(my_file)
            query_sql = """ insert into drugs
                select * from json_populate_recordset(NULL::drugs, %s) """
            cur.execute(query_sql, (json.dumps(data),))
