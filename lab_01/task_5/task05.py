def zig_zag(rows, cols):
    zig_zag_matrix = [] 

    ################### TO DO #########################
    check = 0
    contor = 0

    for i in range(rows):
        vect = []
        for j in range(cols):
            if check == 0:
                if contor <= cols-1: 
                    if j == contor:
                        vect.append(1)
                    else:
                        vect.append(0)
                if j == cols-1:
                    if contor == cols-1 :
                        check=1
                        contor-=1
                    else:    
                        contor+=1
                
            elif check == 1:
                if contor >= 0:
                    if j == contor:
                        vect.append(1)
                    else:
                        vect.append(0)
                if j == cols-1:
                    if contor == 0 :
                        check=0
                        contor+=1
                    else:
                        contor-= 1
        zig_zag_matrix.append(vect)   
    ###################################################

    return zig_zag_matrix
