def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################

    def medie(list):
        sum=0.0
        for i in list:
            sum+=i
        sum/=len(list)
        return sum

    bursa=lambda x: medie(register[x])>=8.5 

    names=list(filter(bursa,register))

    ###################################################
    
    return names
