a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

operation = input('Enter operation: ')

match operation:
    case 'add':
        print(a + b)
    case 'subtract':
        print(a - b)
    case 'multiply':
        print(a * b)
    case 'divide':
        print(a / b)
    case _:
        print("Invalid operation")
