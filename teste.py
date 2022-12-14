#Crie uma função divisivel(mat, primos) que retorna True APENAS se todos os elementos da matriz mat forem divisiveis por algum dos inteiros do vetor primos

def divisivel(mat, primos):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if not any([mat[i][j] % p == 0 for p in primos]):
                return False
    return True

def divisiveis(mat, primos):
    cont = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            atual = mat[i][j]
            for p in primos:
                if atual % p == 0:
                    cont += 1
                    break
    return cont == len(mat) * len(mat[0])
    