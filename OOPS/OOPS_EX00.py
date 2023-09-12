##case1
class student:
    roll = 11
    name = "anupam"
    marks = 100
    def m1(self):
        print("M1->a")
s1 = student()
print(s1.roll)
print(s1.name)
print(s1.marks)

##case 2

class student:
    roll = 2
    name = "anu"
    marks = 90
    def display(self):
        print(self.roll)
        print(self.name)
        print(self.marks)
s2 = student()
s2.roll = 8
s2.name="vipin"
s2.marks = 60
s2.display()
