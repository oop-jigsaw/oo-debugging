from src.store import store

class Student:
    def __init__(self, name = '', hometown = '', school = ''):
        self.name = name
        self.hometown = hometown
        self.school = school
        if self.school:
            self.school_id = school.id
        self.id = len(store['students'])