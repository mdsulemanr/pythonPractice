def get_average():
    numbers = []

    print('Please type a number and hit enter (when you are finished, type done)')
    while True:
        inp = input('Enter a number: ').strip().lower()
        if inp == 'done':
            break
        try:
            numbers.append(float(inp))
        except ValueError:
            print("Invalid input!")

    if not numbers:
        return "No numbers entered."

    return f"Average: {sum(numbers) / len(numbers)}"


print(get_average())
