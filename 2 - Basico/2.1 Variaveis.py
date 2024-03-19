import string
import sys

intval = 42
floatVal = 3.14
boolVal = False
charvar = 'A'
stringvar = "Hello world"

#deve-se printar do mesmo tipo!
print(str() +" "+str(intval)+" "+str(floatVal) +" "+str(boolVal) +" "+str(charvar) +" "+str(stringvar) )

#tamanho de cada elemento de memoria
print(sys.getsizeof(intval))