from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8mb4"

# SQLAlchemyのエンジンを作成
db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# ベースクラスを作成
Base = declarative_base()

# データベースのセッションを取得→DBへのアクセスを可能にする
def get_db():
    with db_session() as session:
        yield session
