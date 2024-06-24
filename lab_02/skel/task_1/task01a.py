def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []

    ################### TO DO #########################
    def fct(x):
        if x%6==0 :
            x*=2
        else:
            x*=3
        return x
    
    result=list(map(fct,nums))

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
