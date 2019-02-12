import loader as loader
import pickle
print("how many options?")
minlen = int(input())
combo  = loader.iter4(minlen)

f = open("runs.txt", "w")
f.write("\n".join(map(lambda x: str(x), combo)))
f.close()

