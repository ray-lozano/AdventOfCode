# Create the two lists for storing data.
list_one = []
list_two = []

path = "day_one.txt"

def read_file()
# Open the day_one text file
try:
    file = open(path)
    f = file.readlines()
except FileNotFoundError:
    print("File not found.")

def append_columns(list_one, list_two, f):
    """Append the columns to their respective lists, then convert the lists to ints."""
    # Append the columns to their respective lists.
    for i in f:
        list_one.append(i.split()[0])
        list_two.append(i.split()[1])

    # Convert both lists to ints.
    for i in range(len(list_one)):
        list_one[i] = int(list_one[i])
        list_two[i] = int(list_two[i])

    # Sort the lists.
    list_one.sort()
    list_two.sort()


    return list_one, list_two


append_columns(list_one, list_two, f)

# Iterate through each value of the sorted list,
# then take the absolute value of the difference
# and add it to the solution variable.
solution = 0
for i in range(len(list_one)):
    temp = abs(list_one[i] - list_two[i])
    solution += temp
    #print(solution)

print(solution)