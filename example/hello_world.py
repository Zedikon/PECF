# Hello world on PECF 1.0.25

import PECF as pecf

main = "world: Hello, str hello: world! str"
print(pecf.decode(main, "world") + " " + pecf.decode(main, "hello"))
