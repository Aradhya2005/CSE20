def make_dictionary(number):
    data = {}
    for _ in range(number):
        try:
            entry = input().strip().split(', ')
            name, major = entry[0], entry[1]
            data[name] = major
        except IndexError:
            pass
    return data

if __name__ == '__main__':
    d = make_dictionary(3)
    print(d)
