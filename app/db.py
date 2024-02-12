from datetime import date

from sqlalchemy import Column, Date, Float, Integer, MetaData, create_engine
from sqlalchemy.orm import Mapped, declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app import config

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(table_name)s_%(column_0_N_name)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=metadata)
engine = create_engine(config.DB_URL)
if not database_exists(engine.url):
    create_database(engine.url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SomeResearch(Base):
    __tablename__ = "some_research"

    id: Mapped[int] = Column(Integer, primary_key=True)
    date: Mapped[date] = Column(Date, nullable=False)
    respondent: Mapped[int] = Column(Integer, nullable=False)
    sex: Mapped[int] = Column(Integer, nullable=False)
    age: Mapped[int] = Column(Integer, nullable=False)
    weight: Mapped[float] = Column(Float, nullable=False)
