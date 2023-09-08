# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
counter1 = Counter(class1)
counter2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(counter1["James"], "James in class 1")

# TODO: How many students are in class 1?
print(sum(counter1.values()), "students in class 1")

# TODO: Combine the two classes
counter1.update(class2)
print(sum(counter1.values()), "total students (class1 + class2)")

# TODO: What's the most common name in the two classes?
print(counter1.most_common(1),"Most common name in both classes")

# TODO: Separate the classes again
counter1.subtract(class2)

# TODO: What's common between the two classes?
print(counter1 & counter2, "Intersection in classes 1 and 2")