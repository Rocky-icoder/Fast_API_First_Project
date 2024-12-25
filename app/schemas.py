from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age : int

class StudentCreate(BaseModel):
    name: str
    age: int


class StudentMarksCreate(BaseModel):
    # student_id: int
    subject: str
    marks: int

class StudentCoursesCreate(BaseModel):
    student_id: int
    course_name: str