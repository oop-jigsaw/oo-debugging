from src import School, Student, store, Teacher


def test_initializes_with_name():
    school = School('William Tennent')
    assert school.name ==  'William Tennent'

    second_school = School('Klinger Middle School')
    assert school.name ==  'Klinger Middle School'

def test_initializes_with_address():
    school = School('William Tennent', '125 Maple Road')
    assert school.address ==  '125 Maple Road'

def test_initializing_a_school_increments_an_underscore_id():
    # reset store
    store['schools'] = [1]
    # done resetting store

    school = School('William Tennent', '125 Maple Road')
    assert school.id == 1
    
    new_school = School('Klinger', '521 Birch')
    assert new_school.id == 2

def test_initializing_a_school_adds_a_new_school_to_the_store():
    store['schools'] = []
    store['students'] = []
    # done resetting store
    school = School('William Tennent', '125 Maple')
    assert school in store['students']

def test_students_method_returns_all_associated_students():
    store['students'] = []

    store['schools'] = []
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    other_school = School('Klinger', '521 Birch Street')
    student = Student('Sam Smith', 'NYC', school)
    other_student = Student('Ben Kingsley', 'NYC', school)
    final_student = Student('Ethan Hawke', 'NYC', other_school)
    assert student in school.students() 
    assert other_student in school.students() 

def test_teachers_method_returns_all_associated_teachers():
    store['students'] = []

    store['schools'] = []
    store['teachers'] = []
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    other_school = School('Klinger', '521 Birch Street')
    teacher = Teacher('Sam Smith', 'NYC')
    other_teacher = Teacher('Ben Kingsley', 'NYC')
    
    final_teacher = Teacher('Ethan Hawke', 'NYC', other_school)
    
    assert teacher in school.teachers() 
    
    assert other_teacher in school.teachers() 


