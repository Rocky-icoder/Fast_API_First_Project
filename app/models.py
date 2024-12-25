from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


# class Student(Base):
#     __tablename__ = "students_name"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, index=True)
#     age = Column(Integer)
#     extra = Column(Integer)

class StudentName(Base):
    __tablename__ = "student_name"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    age = Column(Integer)

    marks = relationship("StudentMarks", back_populates="student")

    # # Relationship to student_courses
    courses = relationship("StudentCourses", back_populates="student")


class StudentMark(Base):
    __tablename__ = "student_mark"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student_name.id"), nullable=False)
    subject = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)

    student = relationship("StudentName", back_populates="marks")

class StudentCourses(Base):
    __tablename__ = "student_courses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student_name.id"), nullable=False)
    course_name = Column(String, nullable=False)

    # Define the relationship to the StudentName table
    student = relationship("StudentName", back_populates="courses")