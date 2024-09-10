from cl_coche import Coche

#Instancia
coche_uno = Coche("Honda", "Civic", 2022)
coche_uno.mostrar_info()
print("Antigüedad: ", coche_uno.edad_auto(), "años")

print("****************************")

coche_dos = Coche("Audi", "TT", 2016)
coche_dos.mostrar_info()
print("Antigüedad: ", coche_dos.edad_auto(), "años")

print("****************************")

coche_tres = Coche("Nissan", "350Z", 2007)
coche_tres.mostrar_info()
print("Antigüedad: ", coche_tres.edad_auto(), "años")

