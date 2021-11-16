from store import store
class School:
    def __init__(self, name = '', address = ''):
        store['school_counter'] += 1
        store['schools'].append(self)
        self._name = name
        self._address = address
        self._id = store['school_counter']
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def students(self):
        students = store['students']
        return [student for student in students if student._school_id == self._id]

    def teachers(self):
        teachers = store['teachers']
        return [teacher for teacher in teachers if teacher._school_id == self._id]
        