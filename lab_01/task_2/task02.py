def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """

    final_nume=[]
    final_prenume=[]
    final_prenume1=[]

    ################### TO DO #########################

    for i in range(len(nume_complete)):
        aux=nume_complete[i].split(" ")
        final_nume.append(aux[0])
        aux=aux[1].split("-")
        final_prenume.append(aux[0])
        final_prenume1.append(aux[1])

    nume_formatat=(final_nume,final_prenume, final_prenume1 )

    ###################################################

    return nume_formatat

    