from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:your_password@localhost/email_automation")

conn = engine.connect()