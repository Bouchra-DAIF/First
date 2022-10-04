d = input("Entrez la densité : ")
VC = input("Entrez la valeur de la viscosité Cénimatique en St :")
try:
    d = float(d)
    VC = float(VC)
    u = VC*1000*d*10**-4
    print("La viscosité dynamique est : ",u, "PI")
except:
    print("la valeur de la densité et/ou la viscosité cénimatique")


