import csv
from collections import namedtuple

Nota = namedtuple("notas", ["ling", "cn", "mat", "ch", "red"])

pesos_medicina = csv.reader(open("./pesos_medicina.csv", "r"))

# NOTE: colocar isso daqui em um arquivo de configuração talvez?
minhas_notas = Nota(ling=649.1, cn=675.1, mat=921.4, ch=685.6, red=820)

notas_duda = Nota(ling=630, ch=711.6, cn=675.7, mat=753.2, red=780)

def media(nota):
    return sum(nota) / 5

def media_ponderada(nota, pred, pcn, pch, pling, pmat):
    soma = (nota.ling * pling) + (nota.cn * pcn) + (nota.mat * pmat) + (nota.red * pred) + (nota.ch * pch)
    return soma / (pling + pcn + pmat + pch + pred)

def recalcular(pesos, nota):
    header = next(pesos)
    media_bruta = media(nota)

    for faculdade in pesos:
        inst = faculdade[0]
        recalculada = media_ponderada(nota, *[float(p) for p in faculdade[1:]])
        print(f"{inst}: {media_bruta} -> {recalculada}")

def main():
    recalcular(pesos_medicina, notas_duda)

if __name__ == "__main__":
    main()
