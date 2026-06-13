# -------------SETS & TUPLE---------------
# Sets automatically handle uniqueness
languages = {"Python", "Java", "C++", "Python", "JavaScript", "Java"}
print("Unique languages:", languages)

# Create another set and perform union, intersection, difference
more_langs = {"Swift", "Python", "Go"}
print("Union:", languages | more_langs)
print("Intersection:", languages & more_langs)
print("Difference:", languages - more_langs)

# Create a tuple of 5 city names
cities = ("Mumbai", "Delhi", "Bhopal", "Pune", "Bhopal")

# Count occurrences, find index, and check existence
print("Bhopal occurs:", cities.count("Bhopal"), "times")
print("Index of Delhi:", cities.index("Delhi"))
print("Is Pune in tuple?", "Pune" in cities)

# modify the tuple and handle the error
try:
    cities[0] = "Indore"
except TypeError as e:
    print(f"Error: {e}. Tuples are immutable!")
