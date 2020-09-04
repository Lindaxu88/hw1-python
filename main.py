# Author: Yeman Xu ybx5148@psu.edu
# Collaborator: Shiao Zhuang sqz5328@psu.edu
# Collaborator: Zhihong Jiang zbj5088@psu.edu

Grade1 = input("Enter your course 1 letter grade: ")
if Grade1 == "A":
   GP = 4.0
elif Grade1 == "A-":
   GP = 3.67
elif Grade1 == "B+":
   GP = 3.33
elif Grade1 == "B":
   GP = 3.0
elif Grade1 == "B-":
   GP = 2.67
elif Grade1 == "C+":
   GP = 2.33
elif Grade1 == "C":
   GP = 2.0
elif Grade1 == "D":
   GP = 1.0
elif Grade1 == "F":
   GP = 0.0
else:
   GP = 0.0
try:
  Credit1 = float(input("Enter your course 1 credit: "))
except:
  GP = 0.0
  Credit1 = 0.0
print(f"Grade point for course 1 is：{GP}")

Grade2 = input("Enter your course 2 letter grade: ")
if Grade2 == "A":
   GP2 = 4.0
elif Grade2 == "A-":
   GP2 = 3.67
elif Grade2 == "B+":
   GP2 = 3.33
elif Grade2 == "B":
   GP2 = 3.0
elif Grade2 == "B-":
   GP2 = 2.67
elif Grade2 == "C+":
   GP2 = 2.33
elif Grade2 == "C":
   GP2 = 2.0
elif Grade2 == "D":
   GP2 = 1.0
elif Grade2 == "F":
   GP2 = 0.0
else:
   GP2 = 0.0
try:
  Credit2 = float(input("Enter your course 2 credit: "))
except:
  GP2=0.0
  Credit2=0.0
print(f"Grade point for course 2 is: {GP2}")

Grade3 = input("Enter your course 3 letter grade: ")
if Grade3 == "A":
   GP3 = 4.0
elif Grade3 == "A-":
   GP3 = 3.67
elif Grade3 == "B+":
   GP3 = 3.33
elif Grade3 == "B":
   GP3 = 3.0
elif Grade3 == "B-":
   GP3 = 2.67
elif Grade3 == "C+":
   GP3 = 2.33
elif Grade3 == "C":
   GP3 = 2.0
elif Grade3 == "D":
   GP3 = 1.0
elif Grade3 == "F":
   GP3 = 0.0
else:
   GP3 = 0.0
try:
  Credit3 = float(input("Enter your course 3 credit:"))
except:
  GP3 = 0.0
  Credit3 = 0.0
print(f"Grade point for course 3 is: {GP3}")

GPA = ((GP * Credit1) + (GP2 * Credit2) + (GP3 * Credit3)) / (Credit1 + Credit2 + Credit3)
print(f"Your GPA is:{GPA}")
