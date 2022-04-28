file_name = "./infile.txt"
infile = open(file_name, "r")

for line in infile:
    print("Line: ", line)
names = [line.rstrip() for line in infile] 
print("names: ", names)
infile.close

def display_with_forloop(file_name):
    infile = open(file_name, "r")
    items = [line.rstrip() for line in infile]
    for line in infile:
        print(line, items)
    infile.close()

def open_file(file_name, mode):
    return open(file_name, "r")
main()
