#check whether a student has passed.if passed,check whether the student has distinction.

marks = int(input('enter student marks:'))

if(marks >= 35):
    print('student is passed')

    if(marks >= 70):
        print('student is distinction')

    else:
        print('student is not distinction')

else:
    print('student is failed')            