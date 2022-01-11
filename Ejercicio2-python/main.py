import re
# Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
#
# 1) Añadir a cualquier persona, indicando nombre y después teléfono
# 2) Buscar el teléfono de una persona

# Ampliación:
#
# - Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido.Ejemplo:
# Introduce un nombre: Pep
# Resultados:
# - Pepe 659331013
# - Pepe Martín 633743551

def main():
    pass

contacts = {}

def addContact ():

    print('- Introduzca nombre y número de teléfono para añadir un contacto')
    print('- Nombre de contacto: ')
    name = input()
    print('- Número de teléfono: ')
    phone = input()
    if phone.isnumeric() & (len(phone) == 9):
        global contacts
        contacts.update({name : phone})
        optionsMenu()
        return contacts
    else:
        print('NÚMERO INCORRECTO')
        optionsMenu()

def findContact():
    global contacts
    print('- Introduzca el nombre del contacto que desea encontrar:')
    searchName = input()
    # contacts.keys()
    pattern = searchName.casefold() + '.*'
    filtered = []
    for contact in contacts.keys():
        if re.match(pattern, contact.casefold()):
            filtered.append(contact)

    for x in filtered:
        print('- Nombre de contacto: ', x, '- Teléfono: ', contacts.get(x))
    return optionsMenu()


def optionsMenu():
    print('- Introduzca 1 si desea añadir un contacto.\n'
          '- Introduzca 2 si desea buscar un contacto.')

    menuOption = input()
    if menuOption == '1':
        addContact()

    if menuOption == '2':
        findContact()

    else:
        print('- Introduzca una opción correcta')

optionsMenu()

if __name__ == '__main__':
    main()
