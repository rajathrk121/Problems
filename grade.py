mark=int(input("Enter your mark: "))

# if mark >=90 and mark<100:
#     print("A GRADE")
# elif mark>=80 and mark<90:
#     print("B GRADE")
# elif mark>=70 and mark<80:
#     print("C GRADE")
# elif mark>60 and mark<70:
#     print("D GRADE")
# elif mark<=60 and mark>0:
#     print("F")
# else:
#     print("Invalid Marks")

if mark>100 or mark <0:
    print("Enter a valid mark")
elif mark>=90:
    print("A GRADE")
elif mark>=80:
    print("B GRADE")
elif mark>=70:
    print("C GRADE")
elif mark>=60:
    print("D GRADE")
else:
    print("F")