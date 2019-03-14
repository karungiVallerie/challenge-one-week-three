x = input('enter a string, float,integer: ')

character = []
def sort_list(list_input):

    for v in list_input:
        if isinstance (v,str):
            character.append(v)#means to add on v
            print(character)
