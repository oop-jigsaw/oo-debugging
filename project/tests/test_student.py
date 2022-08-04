from src import Student, School, store

def test_can_create_student():
    assert type(Student()) == Student

def test_initializes_with_name():
    student = Student('Sam Smith')
    assert student.name ==  'Sam Smith'

def test_initializes_with_hometown():
    student = Student('Sam Smith', 'NYC')
    assert student.hometown ==  'NYC'

def test_name_returns_name():
    student = Student('William Tennent', '125 Maple Road')
    assert student.name ==  'William Tennent'

def test_address_return_address():
    student = Student('Sam Smith', 'NYC')
    assert student.hometown ==  'NYC'

def test_initializing_a_student_increments_an_underscore_id():
    # reset store
    store['students'] = []
    # done resetting store

    student = Student('Sam Smith', 'NYC')
    assert student.id == 1

    new_student = Student('Ben Kingsley', 'Philadelphia')
    assert new_student.id == 2

def test_id_returns_id():
    # reset store
    store['students'] = []
    # done resetting store
    student = Student('Sam Smith', 'NYC')
    assert student.id == 1

def test_initializing_a_student_adds_a_new_student_to_the_store():
    store['students'] = []
    # done resetting store
    student = Student('Sam Smith', 'NYC')
    assert store['students'][0] == student

def test_school_id_stored_as_attribute():
    store['students'] = []

    store['schools'] = []
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    student = Student('Sam Smith', 'NYC', school)
    assert student.school_id == 1