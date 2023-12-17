def get_data():
    while True:
        try:
            user_input = float(input("Enter a number:"))
            return user_input
        except ValueError:
            print("It is not a number!")

if __name__ == '__main__':
    n = get_data()
    assert type(n) == float
    print(f'{n} is a number.')
