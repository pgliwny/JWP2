from sqlalchemy import create_engine, Column, Integer, String, text, Float
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite+pysqlite:///:memory:')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(Float)

Base.metadata.create_all(engine)

with Session(engine) as session:
    new_user = Student(name="Jan Kowalski", grade=2.0)
    session.add(new_user)
    new_user = Student(name="Jan Kowalski1", grade=3.0)
    session.add(new_user)
    new_user = Student(name="Jan Kowalski2", grade=4.0)
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    students = session.execute(text("SELECT * FROM students")).all()
    for student in students:
        print(f'{student.name}, {student.grade}')

def addStudent(name, grade):
    with Session(engine) as session:
        new_user = Student(name=name, grade=grade)
        session.add(new_user)
        session.commit()

def updateStudent(id, name, grade):
    with Session(engine) as session:
        student_to_update = session.get(Student, id)
        if student_to_update:
            student_to_update.name = name
            student_to_update.grade = grade
            session.commit()

def readStudents():
    with Session(engine) as session:
        students = session.execute(text("SELECT * FROM students")).all()
        for student in students:
            print(f'{student.name}, {student.grade}')

def deleteStudent():
    with Session(engine) as session:
        student_to_delete = session.get(Student, 1)
        if student_to_delete:
            session.delete(student_to_delete)
            session.commit()
