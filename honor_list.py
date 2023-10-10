#formulate honor list
#import math *
grades={}
index=0
x=(int(input('Enter the number of subject : ')))
while index < x:
    subject=input('Enter subject name : ')
    Grade=float(input('Enter ' + subject + ' Grade : '))
   # Grade=float(Grade)
    grades[subject]=Grade
    index=index+1

print(grades)
print()
GPA=float(sum(grades.values()))
GPA=(GPA/x)
print('YOUR GPA IS ' + str(GPA))
min_grade=min(grades.values())
print('MINIMUM GRADE IS ' + str(min_grade))
max_grade=max(grades.values())
print('MAXIMUM GRADE IS ' + str(max_grade))
print()
if GPA>=80 and min_grade >=70:
    First_Class = True
else:
    First_Class = False

if First_Class:
    string=('Congratulations you made First Class Honors!!!')
    print (string.upper())