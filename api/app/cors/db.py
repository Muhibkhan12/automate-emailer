from sqlalchemy import create_engine
import json

engine = create_engine("mysql+pymysql://root:your_password@localhost/email_automation")


try:
    conn = engine.connect()
    print({"message":"Sql Connected successfully"})
    conn.close()
except Exception as e:
    print({
        "error": str(e)
    })