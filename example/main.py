# for version 1.0.25
import PECF as pecf

hehe = open("main.pecf").read()
a = pecf.decode(hehe, "hehe")
print(a)

# for version 1.0.26
import PECF as pecf

hehe = open("main.pecf").read()
a = pecf.load(hehe)
b = pecf.decode("hehe")
print(b)
