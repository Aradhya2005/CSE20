
def copy(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
    except IOError as e:
        print(f"An error occurred: {e}")
        
if __name__ == '__main__':

    copy("my.txt.", "my_copy.txt")
    count, same, dif = 1, 0, 0
    with open("my.txt", "r") as f1, open("my_copy.txt", "r") as f2:
        file1 = f1.readlines()
        file2 = f2.readlines()
        
    for i in range(len(file1)):
        print(f'line {count}: {file1[i].rstrip()} -- {file2[i].rstrip()}')
        if file1[i] == file2[i]:
            print(f"lines are the same.")
            same += 1
        else:
            print(f"lines are different.")  
            dif += 1
        count += 1
    assert dif == 0
    assert same != 0


