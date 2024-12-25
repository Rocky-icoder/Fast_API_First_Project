from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app import models, schemas
from app.models import StudentName, StudentMark, StudentCourses

from app.schemas import StudentCreate, StudentMarksCreate, StudentCoursesCreate

router = APIRouter()

@router.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.StudentName).all()
    return students


@router.post("/students/", status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Create a new Student instance
    new_student = StudentName(
        name=student.name,
        age=student.age)

    db.add(new_student)  # Add the new student to the session
    db.commit()          # Commit to save the data
    db.refresh(new_student)  # Refresh to get the new ID
    return new_student     # Return the stored student data



@router.post("/student_marks/")
def add_student_marks(marks: schemas.StudentMarksCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.StudentName).filter(models.StudentName.id == marks.student_id).first()
    if db_student:
        db_marks = models.StudentMark(student_id=marks.student_id, subject=marks.subject, marks=marks.marks)
        db.add(db_marks)
        db.commit()
        db.refresh(db_marks)
        return db_marks
    else:
        raise HTTPException(status_code=404, detail="Student not found")

