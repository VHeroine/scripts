class Student:
    """Class student who is passed a course.
    May or not learn hard skills.
    May or not work after the course.
    """
    __nes_skills = {
        'English',
        'Sql',
        'Linux',
        'Python'
    }

    def __init__(self, name, surname, height):
        self.name = name
        self.surname = surname
        self.height = height
        self.skills = {'English': True,
                       'Sql': False,
                       'Linux': False,
                       'Python': False}
        self.enter_course()
    
    def enter_course(self):
        print(f'Student {self.name} {self.surname} entered to the course.')
    
    def learning(self, skill):
        self.skills[skill.capitalize()] = True
    
    def job(self):
        if False in (self.skills[key] for key in self.__nes_skills):
            print(f'Student {self.name} {self.surname} was not hired a job.')
        else:
            print(f'Student {self.name} {self.surname} was hired a job.')

# Taking and teaching the first student.
a = Student('Joey', 'Santana', 21)
a.learning('SQL')
a.learning('Linux')
a.learning('Python')

# Taking and teaching the second student.
b = Student('Igor', 'Suxov', 22)
b.learning('SQL')
b.learning('Linux')
b.learning('Python')

# Taking and teaching the third student.
c = Student('Denis', 'Tankov', 20)
c.learning('SQL')
c.learning('Linux')

# Break a line
print()

# Trying to hire them.
a.job()
b.job()
c.job()