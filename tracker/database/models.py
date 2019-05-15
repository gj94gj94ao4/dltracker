from dataclasses import dataclass

from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from . import Base

association_table = Table('works_cvs', Base.metadata,
                          Column('work_rjnumber', String(10),
                                 ForeignKey('works.rjnumber')),
                          Column('cv_id', Integer, ForeignKey('cvs.id'))
                          )


@dataclass
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    rjnumber = Column(String(10), ForeignKey('works.rjnumber'))
    work = relationship("Work", back_populates="records")
    timestamp = Column(DateTime)
    dlcount = Column(Integer)
    favoritecount = Column(Integer)


@dataclass
class CV(Base):
    __tablename__ = 'cvs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    works = relationship(
        "Work",
        secondary=association_table,
        back_populates="cvs"
    )


@dataclass
class Work(Base):
    __tablename__ = 'works'
    rjnumber = Column(String(10), primary_key=True, unique=True)
    name = Column(String(200))
    club = Column(String(60), unique=True)
    series = Column(String(200), nullable=True)
    records = relationship("Record", back_populates="work")
    publish_date = Column(DateTime)
    cvs = relationship(
        "CV",
        secondary=association_table,
        back_populates="works"
    )
