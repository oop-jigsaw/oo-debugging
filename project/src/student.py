from store import store
from school import School
class Student:
    def __init__(self, name = '', hometown = '', school = ''):
        store['students'].append(self)
        self.name = name
        self.hometown = hometown
        self.school = school
        if self.school:
            self.school_id = school.id
        self.id = len(store['students'])