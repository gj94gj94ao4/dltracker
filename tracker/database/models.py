from dataclasses import dataclass

from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from typing import List

from . import Base

association_table = Table('works_cvs', Base.metadata,
                          Column('work_uid', String(10),
                                 ForeignKey('works.uid')),
                          Column('cv_id', Integer, ForeignKey('cvs.id'))
                          )


@dataclass
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    uid = Column(String(10), ForeignKey('works.uid'))
    work = relationship("Work", back_populates="records")
    timestamp:DateTime = Column(DateTime)
    dl_count:int = Column(Integer)
    wishlist_count:int = Column(Integer)


@dataclass
class CV(Base):
    __tablename__ = 'cvs'
    id = Column(Integer, primary_key=True)
    name:str = Column(String(50))
    works = relationship(
        "Work",
        secondary=association_table,
        back_populates="cvs"
    )


@dataclass
class Work(Base):
    __tablename__ = 'works'
    uid:str = Column(String(10), primary_key=True, unique=True)
    name:str = Column(String(200))
    club:str = Column(String(60))
    series:str = Column(String(200), nullable=True)
    records:Record = relationship("Record", back_populates="work")
    publish_date:DateTime = Column(DateTime)
    cvs:CV = relationship(
        "CV",
        secondary=association_table,
        back_populates="works"
    )
