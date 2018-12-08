from sys import argv

script, from_f, to_f = argv

open(to_f,'w').write(open(from_f).read())

open(from_f).close()
open(to_f).close()
