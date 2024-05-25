# Definimos una función para el cifrado que acepta 3 parámetros
# Text: Texto a cifrar/descifrar
# Offset: Clave de encriptación
# Direction: Determina si se cifrará o descifrará (1=Cifrar,-1=Descifrar)
def cypher(text, offset, direction=1):
    # Se inician 2 strings con las letras del alfabeto en minúscula y mayúscula y el mensaje final
    alphabet='abcdefghijklmnñopqrstuvwxyz'
    alphabetupper=alphabet.upper()
    final_message=''

    # Por cada caracter en el texto lleva a cabo la sustitución
    for char in text:
        # Verifica si el caracter es alfanumerico, en caso de no serlo solo agrega el caracter al mensaje final
        if not char.isalpha():
            final_message += char
        else:
            # En casi sí sea alfanumerico, verifica su posición dentro del alfabeto para obtener el índice
            index = alphabet.find(char.lower())
            # Crea una variable new_index en donde se cambia el índice según la clave solicitada y hace un módulo con la longitud del alfabeto
            new_index = (index + offset*direction) % len(alphabet)
            # Si el caracter está en minúscula toma el nuevo índice y lo busca en el alfabeto en minúscula
            if char.islower():
                final_message += alphabet[new_index]
            else:
                # En caso contrario lo busca en el alfabeto en mayúscula
                final_message += alphabetupper[new_index]
    # Retorna el mensaje final
    return final_message

# Se inicializa una variable llamada encrypt que llama a la función cypher con direction=1 para encriptar
def encrypt(text,offset):
    try:
        if (offset>0,text!=''):
            result = cypher(text,offset)
            return result
        else:
            return 'Por favor complete los campos'
    except Exception:
        return "Por favor complete correctamente los campos"
    
# Se inicializa una variable llamada decrypt que llama a la función cypher con direction=-1 para desencriptar
def decrypt(text,offset):
    try:
        if (offset>0,text!=''):
            result = cypher(text,offset,-1)
            return result
        else:
            return 'Por favor complete los campos'
    except Exception:
        return "Por favor complete correctamente los campos"