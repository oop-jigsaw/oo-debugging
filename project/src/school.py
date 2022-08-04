from store import store
class School:
    def __init__(self, name = '', address = ''):
        self.name = name
        self.address = address
        store['schools'].append(self)
        self.id = len(store['schools'])
        
    def teachers(self):
        return [teacher for teacher in store['teachers'] if teacher.school_id == self.id]

    def students(self):
        return [student for student in store['students'] if student.school_id == self.id]
