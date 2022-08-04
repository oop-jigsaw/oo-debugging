from store import store
class Teacher:
    def __init__(self, name = '', hometown = '', school = ''):
        store['teachers'].append(self)
        self.name = name
        self.hometown = hometown
        self.school = school
        if school:
            self.school_id = school.id
        self.id = len(store['teachers'])