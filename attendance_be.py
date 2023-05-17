from attendance import *


def add_teacher():
    f_name = input("Insert teachers name: ")
    l_name = input("Insert teachers last name: ")
    subject = input("Insert teachers subject: ")
    teacher = Teacher(f_name=f_name, l_name=l_name, subject=subject)
    session.add_all([teacher])
    session.commit()
    print(f"{f_name} {l_name} was created")


def add_student():
    f_name = input("Insert Students name: ")
    l_name = input("Insert Students last name: ")
    student = Student(student_fname=f_name, student_lname=l_name)
    session.add_all([student])
    session.commit()
    print(f"{f_name} {l_name} was created")


def add_status():
    status_name = input("insert status name: ")
    status = AttStatus(name=status_name)
    session.add_all([status])
    session.commit()
    print(f"{status_name} was created")


def get_choices(a_class):
    options = session.query(a_class).all()
    for a in options:
        print(a)


def get_lessons():
    lessons = session.query(Lesson).all()
    for lesson in lessons:
        print(lesson.id, lesson.teacher.f_name, lesson.teacher.l_name, lesson.date_)


def create_lesson():
    get_choices(Teacher)
    choosen_teacher = input("Choose teacher: ")
    today_date = datetime.strptime(
        input("Insert day of lesson (YYYY-MM-DD): "), "%Y-%m-%d"
    )
    t_date = Lesson(date_=today_date, teacher_id=choosen_teacher)
    session.add_all([t_date])
    session.commit()


def check_attendance():
    get_lessons()
    chosen_lesson = input("Choose lesson: ")
    get_choices(Student)
    while True:
        chosen_student = input("Choose student or insert 0 to finish: ")
        if chosen_student == "0":
            break
        else:
            get_choices(AttStatus)
            chosen_status = input("Isert attendance status: ")
            student_atendance = StudentAttendance(
                lesson_id=chosen_lesson,
                student_id=chosen_student,
                attstatus_id=chosen_status,
            )
            session.add_all([student_atendance])
            session.commit()
            continue
        