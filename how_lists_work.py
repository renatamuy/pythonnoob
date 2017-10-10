'''How lists work in Python'''


#compare the outputs


animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]

for x in range(len(animais)):
    print("--> ", animais[x])

for x in animais:
    print("--> " + x)

for x in animais:
    print("--> ", x-1)

for x in range(len(animais)):
    print("--> ", x)

for x in animais:
    print("--> ", x)
