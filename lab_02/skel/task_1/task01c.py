def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################
    
    def pal(cuv):
        if cuv == cuv[::-1] :
            return 1
        return 0
    palindromes=list(filter(pal,words))
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
