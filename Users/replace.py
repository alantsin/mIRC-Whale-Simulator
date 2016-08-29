import sys
import codecs

argfile = str(sys.argv[1])

f = codecs.open(argfile, "r", encoding='utf-8')
contents = f.read()

print(contents, "\n")

newcontents = contents.replace("\"", "\'")

f.close()

f2 = codecs.open(argfile, "w", encoding='utf-8')
f2.write(newcontents)

print(newcontents)

f2.close()
