from email import message


def response(input_message):
    message = input_message.lower()

    match message:
        case 'nice':
            return 'very nice lol'
    
        case 'hello':
            return 'hello'
        case _:
            return 'teste'
