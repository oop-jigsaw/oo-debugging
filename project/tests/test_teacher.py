from code import Teacher, School, store

def test_can_create_teacher():
    assert type(Teacher()) == Teacher

def test_initializes_with_name():
    teacher = Teacher('Strauss')
    assert teacher._name ==  'Strauss'

def test_initializes_with_hometown():
    teacher = Teacher('Sam Smith', 'NYC')
    assert teacher._hometown ==  'NYC'

def test_name_returns_name():
    teacher = Teacher('William Tennent', '125 Maple Road')
    assert teacher.name ==  'William Tennent'

def test_address_return_address():
    teacher = Teacher('Sam Smith', 'NYC')
    assert teacher.hometown ==  'NYC'

def test_initializing_a_teacher_increments_an_underscore_id():
    # reset store
    store['teachers'] = []
    store['teacher_counter'] = 0
    # done resetting store

    teacher = Teacher('Sam Smith', 'NYC')
    assert teacher._id == 1

    new_teacher = Teacher('Ben Kingsley', 'Philadelphia')
    assert new_teacher._id == 2

def test_id_returns_id():
    # reset store
    store['teachers'] = []
    store['teacher_counter'] = 0
    # done resetting store
    teacher = Teacher('Sam Smith', 'NYC')
    assert teacher.id == 1

def test_initializing_a_teacher_adds_a_new_teacher_to_the_store():
    store['teachers'] = []
    store['teacher_counter'] = 0
    # done resetting store
    teacher = Teacher('Sam Smith', 'NYC')
    assert store['teachers'][0] == teacher

def test_school_id_stored_as_attribute():
    store['teachers'] = []
    store['teacher_counter'] = 0

    store['schools'] = []
    store['school_counter'] = 0
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    teacher = Teacher('Sam Smith', 'NYC', school)
    assert teacher._school_id == 1

def test_school_returns_related_school_instance():
    store['teachers'] = []
    store['teacher_counter'] = 0

    store['schools'] = []
    store['school_counter'] = 0
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    teacher = Teacher('Sam Smith', 'NYC', school)
    assert teacher.school() == school