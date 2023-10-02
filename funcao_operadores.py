def operator(**kwargs):
    make_float = kwargs.get('make_float', False)
    operation = kwargs.get('operation')
    first = kwargs.get('first')
    second = kwargs.get('second')
    message = kwargs.get('message', None)

    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    elif operation == 'divide':
        if second == 0:
            return "Error: division by zero"
        result = first / second
    else:
        return "Invalid Operation"

    if make_float:
        result = float(result)

    if message:
        return message + str(result)
    else:
        return "Result: " + str(result)