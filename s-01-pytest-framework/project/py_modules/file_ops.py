# open file using the try finally block
try:
    # f is obnnject handling variable
    f = open("myfile.txt", "r")
    # print(f.read())
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    # print(f.readlines())
finally:
    f.close()

# open file using with open statement
print("\n--- Using with open option ---")
with open("myfile.txt", "r") as f:
    # # split contents of file into a list
    # print(f.readline())
    # list2 = f.read().split("\n")
    # print(list2)

    # loop through the f object
    for line in f:
        print(line.strip())