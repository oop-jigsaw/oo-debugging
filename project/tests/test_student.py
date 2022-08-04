from src import Student, School, store

def test_id_returns_id():
    # reset store
    store['students'] = []
    
    student = Student('Sam Smith', 'NYC')
    assert student.id == 1

def test_school_id_stored_as_attribute():
    store['students'] = []

    store['schools'] = []
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    student = Student('Sam Smith', 'NYC', school)
    assert student.school_id == 1