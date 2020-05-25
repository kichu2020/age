age = int(input("What is your child's age? "))
if age < 0:
  print("not born")
elif 0 < age <= 3:
  print("toddler")
elif 3 < age <= 12:
  print("child")
elif 12 < age <= 18:
  print("teenager")
else:
  print("adult")