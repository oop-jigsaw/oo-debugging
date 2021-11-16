from store import store
class Student:
    def __init__(self, name = '', hometown = '', school = ''):
        store['student_counter'] += 1
        store['students'].append(self)
        self._name = name
        self._hometown = hometown
        if school:
            self._school_id = school.id
        self._id = store['student_counter']
    
    @property
    def id(self):
        return self._id
        
    @property
    def name(self):
        return self._name

    @property
    def hometown(self):
        return self._hometown

    def school(self):
        schools = store['schools']
        matching_schools = [school for school in schools if school.id == self._school_id]
        return matching_schools[0]