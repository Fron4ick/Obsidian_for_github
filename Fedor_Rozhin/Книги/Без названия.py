def inN(chislo_in10,osnovanie):

    novoe=0

    kol=1

    while chislo_in10!=0:

        novoe+=(chislo_in10%osnovanie)*kol

        chislo_in10//=osnovanie

        kol*=10

  

    return novoe

  

def kolvo_chisel(chislo):

  

    summa=0

    chislo=str(chislo)

    for i in chislo:summa+=int(i)

    return summa

  

maxxxxa=0

for k in range(502,504):

    a=125**20-5**k+74

    maxxxxa=max(maxxxxa, str(inN(a,5)).count('4'))

    if maxxxxa==100:

        print(k)

        break