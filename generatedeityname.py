from argparse import ArgumentParser
import gibi

args = ArgumentParser()

args.add_argument("--names",type=int,default=1)

ns = args.parse_args()


m = gibi.Matrix()
with open("matrix.gibi","rb") as f:
    m.load(f)

for n in range(ns.names):
    print(m.make_word())

