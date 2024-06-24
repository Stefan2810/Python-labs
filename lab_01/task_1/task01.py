def func(note, nume_materie):
    """
    Trebuie sa creati un tuplu cu numele "pereche",
    in care veti tine, astfel, (media notelor, numele_materiei)
    exemplu: pereche = (...)
    """

    ################### TO DO #########################
    
    medie=0
    for i in range(len(note)):
        medie+=note[i]
    medie/=len(note)
    pereche = ( medie, nume_materie )

    ###################################################

    return pereche
