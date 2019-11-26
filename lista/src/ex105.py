def notas(* notas, sitp=False):
    f = list()
    for n in notas:
        f.append(n)
    f.sort(reverse=True)
    print(f)
    media = sum(f)/len(f)
    sit = 'Aprovadoa' if media > 6 else 'Reprovada'
    ret = {'qtdNotas':len(notas),
           'maiorNota':f[0],
           'menorNota':f[len(f)-1],
           'mediaTurma':media,
           'situacao':sit}

    if sitp == False:
        del ret['situacao']


    return ret

print(notas(33,3,2, 5, 8, 2, 25))
print(notas(0,3,2, 5, 1, 2, 1))
print(notas(0,3,2, 5, 1, 2, 1, sitp=True))
