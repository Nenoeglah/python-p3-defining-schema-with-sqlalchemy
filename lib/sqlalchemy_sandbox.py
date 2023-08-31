
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
 
    engine = create_engine('sqlite:///students.db')

  
    Base.metadata.create_all(engine)

  
    Session = sessionmaker(bind=engine)
    session = Session()

    
    students_to_insert = ['Milgo Chepngeno', 'Eglah Kitty', 'Georgia', 'Ginny']
    for student_name in students_to_insert:
        student = session.query(Student).filter_by(name=student_name).first()
        if not student:
            new_student = Student(name=student_name)
            session.add(new_student)
            session.commit()
            print(f"{student_name} .")


    students = session.query(Student).all()
    print("List of Students:")
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")

   
    session.close()

