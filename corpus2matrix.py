import codecs
import gibi

with codecs.open("corpus.txt","r",encoding="utf-8") as f:
    n = gibi.FrenchNormalizer(f)
    m = gibi.Matrix()
    m.feed(n)

with open("matrix.gibi","wb") as out:
    m.dump(out)

print(m.dict,end="")
print("dumped to matrix.gibi")

