from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

## ----Create Students----#


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)

    teachers = relationship(
        "Teacher", secondary="teachers_to_students", back_populates="students", passive_deletes=True)
    # grade = relationship('Grade', back_populates='students')
    # group = relationship('Group', back_populates='students')

## ----Create teacher----#


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)

    students = relationship(
        "Student", secondary="teachers_to_students", back_populates="teachers", passive_deletes=True)
    #discipline = relationship('Discipline', back_populates='teachers')
    

## ----Create TeacherStubent----#
class TeacherStubent(Base):
    __tablename__ = 'teachers_to_students'
    id = Column(Integer, primary_key=True)
    teacher_id = Column('teacher_id', ForeignKey(
        'teachers.id', ondelete='CASCADE'))
    student_id = Column('student_id', ForeignKey(
        'students.id', ondelete='CASCADE'))

## ----Create Groups_users----#


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    namber = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))

    #student = relationship('Student', back_populates='groups')
    

## ----Create Discipline----#


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    discipline = Column(String(150), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))

    #teacher = relationship('Teacher', back_populates='disciplines')
    #grade = relationship('Grade', back_populates='disciplines')

# ----Create Grade----#
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    discipline = Column(String(150), nullable=True)
    rating = Column(Integer, nullable=True)
    date_gr = Column(DateTime, default=datetime.now())

    #student = relationship('Student', back_populates='grades')
    #discipline = relationship('Discipline', back_populates='grades')