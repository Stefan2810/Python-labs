
def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """

    encoded_message = ""
    ################### TO DO #########################
    
    dictionary={}

    for i in range(26):
        letter = chr(65 + i)
        dictionary[letter] = str(i+1)

    dictionary[' ']=str(0)

    for c in string_message :
        encoded_message +=dictionary[c]

    ###################################################

    return encoded_message
