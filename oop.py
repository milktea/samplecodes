#Object Oriented Programming Test Code
#From Python Web Programming Tutorial
#Milktea

class Program():
    def __init__(self, *args, **kwargs):
	self.lang = raw_input('What Language: ')
	self.version = raw_input('What version: ')
	self.skill = raw_input('What skill level: ')

    def upgrade(self):
	new_version = raw_input('New version: ')
	self.version = new_version

p1 = Program()
print(p1.version)
p1.upgrade()
print(p1.version)
