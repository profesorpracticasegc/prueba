def holamundo(mensaje, x, z):
	if z < 10:
		print "el valor %d es mas pequeno que 10" %(z)

	print "hola mundo " + mensaje + x

def adiosmundo():
	print "adios mundo"

mensaje = "este es un mensaje de prueba, mensaje, 1 2 3, probando"
holamundo(mensaje, "prueba", 8)
adiosmundo()

