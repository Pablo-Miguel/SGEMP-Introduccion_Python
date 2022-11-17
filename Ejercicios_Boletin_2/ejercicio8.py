listaNombres = ["Pablo", "Marta", "Ana", "Manu", "Antonio"]


print(sum(x.lower().startswith("a") for x in listaNombres))