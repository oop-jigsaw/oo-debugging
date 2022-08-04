from src import Teacher, School, store

def test_school_returns_related_school_instance():
    store['teachers'] = []
    
    store['schools'] = []
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    teacher = Teacher('Sam Smith', 'NYC', school)
    assert teacher.school == school