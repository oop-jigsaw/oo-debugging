from src.store import store
class School:
    def __init__(self, name = '', address = ''):
        self.name = 'William Tennent'
        self.address = address
        store['schools'].append(self)
        self.id = len(store['schools'])

    def students(self):
        matching_students = [student for student in store['students'] if student.school == self.id]
        return matching_students

    def teachers(self):
        return [teacher for teacher in store['teachers'] if teacher.school_id == self.id]

    
