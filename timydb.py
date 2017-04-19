import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Interval
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class TimyDbModel(Base):
    # TODO add function to delete all times from the table
    # TODO add also column - time and date created

    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)
    time_measured = Column(Interval, nullable=False)
    order_number = Column(Integer, nullable=False)  # number received from TIMY3 [1-99]

    def __init__(self, time_measured, order_number):
        self.time_measured = time_measured
        self.order_number = order_number

engine = create_engine('sqlite:////Users/ferojanus/Repos/timy_database/db1.sqlite')
Base.metadata.create_all(engine)