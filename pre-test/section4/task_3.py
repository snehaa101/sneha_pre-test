# ----------DICTIONARY OPERATIONS---------
students = {
    1: {"name": "rahul", "age": 21, "marks": 80},
    2: {"name": "tina", "age": 21, "marks": 90},
    3: {"name": "anjali", "age": 21, "marks": 50},
}

# 2) ADD NEW STUDENT AND UPDATE MARKS OF EXSITING

students[4] = {"name": "sneha", "age": 21, "marks": 99}
students[3]["marks"] = 60

# 3) DELETE AND CHECK

del students[3]
print("3 kry exists : ", 3 in students)

# 4) LOOP

for id, info in students.items():
    print(f"id : {id}, info : {info}")

# 5) NAMES LIST
names_list = [info["name"] for info in students.values()]
print("students name : ", names_list)
