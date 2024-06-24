def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################
    
    a=10
    b='a'

    def ascii(char):
        for c in "bcdfghjklmnpqrstvwxyz" :
            if char == c :
                return 1
        return 0
    for i in args:
        if type(i)==type(a) or ascii(i) == 1:
            result.append(i)

    ###################################################
    
    return result
