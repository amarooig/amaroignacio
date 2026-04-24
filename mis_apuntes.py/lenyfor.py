alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = []
slytherin = []
#variables donde se guardaran los con + 5 letras y -5 letras
#definirlas al rato

for alumno in alumnos:  
    if len(alumno) > 5:
        #se va a slytherin por que tiene 5 letras
        slytherin.append(alumno)
    else:
        gryffindor.append(alumno)

print(slytherin)
print(gryffindor)
