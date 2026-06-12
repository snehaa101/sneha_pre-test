# ---------LIST-------------3

# 1) CREATE A LIST 5 STUDENT NAME
students = ["alle", "jolly", "hope", "lily"]

# 2) ADD 2 NAMES
students.append("sneha")  # using append
students.insert(0, "lisa")  # using insert

# 3) REMOVE NAMES
students.remove("alle")  # using remove
students.pop(2)  # usimg pop

# 4) SORT AND PRINT IN REVERSE
students.sort()
print("reverse order : ", students)

# 5) PRINT 1ST 3 ELEMENTS
print("first three elements :", students[:3])
