from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


sqlite_engine = create_engine("sqlite:///sql/base.db", echo=True)
sqlite_session = sessionmaker(autocommit=False, autoflush=False, bind=sqlite_engine)
Base = declarative_base()


def get_db():
    with sqlite_session() as session:
        yield session
