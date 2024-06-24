def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""

    ################### TO DO #########################
    
    def voc(c):
        if c in "aeiou":
            return c.upper()
        return c
    
    new_phrase=list(map(voc,phrase))

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
