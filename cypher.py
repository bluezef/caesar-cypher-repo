def cypher(text, offset, direction=1):
    alphabet='abcdefghijklmnñopqrstuvwxyz'
    final_message=''

    for char in text.lower():
        if not char.isalpha():
            final_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(text,offset):
    try:
        if (offset>0,text!=''):
            result = cypher(text,offset)
            return result
        else:
            return 'Por favor complete los campos'
    except Exception:
        return "Por favor complete correctamente los campos"
def decrypt(text,offset):
    try:
        if (offset>0,text!=''):
            result = cypher(text,offset,-1)
            return result
        else:
            return 'Por favor complete los campos'
    except Exception:
        return "Por favor complete correctamente los campos"