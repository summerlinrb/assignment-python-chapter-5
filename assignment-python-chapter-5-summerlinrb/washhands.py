# Follow the instructions for what to code in this file.


def average1(list1):
    return sum(list1) / len(list1)


def average2(list2):
    return sum(list2) / len(list2)


list1 = [18.1, 15.4, 19.0, 13.4, 10.2, 13.1, 18.1, 14.4, 15.0, 10.8, 5.4, 12.2]
list2 = [0.7, 0.0, 0.7, 1.0, 1.1, 0.4, 0.0, 1.0, 2.3, 2.9, 1.3]

average1 = average1(list1)
average2 = average2(list2)
print(f" Average mortality rate before hand washing policy: {average1}")
print(f" Average mortality rate after hand washing policy: {average2}")
