Gus = {"Nombre": "Yeli ramos", "edad": 17,"salario":6000,"trabajo":"secretario"}
tomanzin = {"Nombre": "Barbara pacheco", "edad": 17,"salario":4000,"trabajo":"limpia baños"}

# print(toño["salario"])
# print(toño["nombre"].split()[-1])

personas = [Gus, tomanzin]

for persona in personas:
    # print(persona["nombre"],persona["edad"], sep ", ")
    tot = sum(persona["salario"] for persona in personas)
print (tot)    