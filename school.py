import copy

class School():
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
        roster[9] = []
        roster[10] = []
        roster[11] = []
        roster[12] = []
     
    def add_student(self, name, grade):
        self.roster[grade].append(name)