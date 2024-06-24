def func(size):

    romb = ""

    ################### TO DO #########################
    #deseneaza un romb de dimensiune size
    
    if size%2==0:
        size+=1

    aux=(size-1)/2
    dim=0

    for i in range(size) :
        c1=aux
        c2=dim
        while(c1>0):
            romb+=' '
            c1-=1
        romb+='@'

        while(c2>0):
            romb+='.'
            c2-=1
        romb+='@\n'
        
        if i < (size-1)/2:
            dim += 2
            aux -= 1
        else:
            dim -= 2
            aux += 1
    ###################################################

    return romb