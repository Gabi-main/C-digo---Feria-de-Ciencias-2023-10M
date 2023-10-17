montos = [450.95,525.67,469.84,230.00]
cuenta = str(input("Introduzca el número de su tarjeta: "))
continuar = True

def funciones (x):
	print("1. REVISAR ESTADO DE CUENTA")
	print("2. RETIRO")
	print("3. INGRESO")
	print("4. COMPRA")
	operacion = int(input("Especifique la operacion que desea realizar: "))
	if operacion == 1:
		print("Su tarjeta actualmente cuenta con ",x," dólares.")
	elif operacion == 2:
		monto = float(input("Cuánto desea retirar?: "))
		x -= monto
		print("IMPRIMIENDO...")
		print("Su tarjeta ahora cuenta con ",x," dólares.")
	elif operacion == 3:
		monto = float(input("Cuánto desea ingresar?: "))
		x += monto
		print("PROCESANDO...")
		print("Su tarjeta ahora cuenta con ",x," dólares.")
	elif operacion == 4:
		print("1.RECARGA TELEFÓNICA")
		print("2. FACTURA DEL AGUA")
		print("3. FACTURA DE LA LUZ")
		print("4. OTRO")
		com = int(input("Qué desea comprar? :  "))
		if com == 1:
			y = "recarga telefónica"
		if com == 2:
			y = "factura del agua"
		if com == 3:
			y = "factura de la luz"
		if com == 4:
			y = "artículo en línea"
		monto = float(input("Cual es el monto?:   "))
		x -= monto
		print("IMPRIMIENDO...")
		print("Su tarjeta ahora cuenta con ",x," dólares luego de la compra de ", y)
	return(x)
		
while continuar == True:
		if cuenta == "2470819178945567":
			montos[0] = funciones(montos[0])
		if cuenta == "5075414456789335":
			montos[1] = funciones(montos[1])
		if cuenta == "4048769875457643":
			montos[2] = funciones(montos[2])
		if cuenta == "378135672298473":
			montos[3] = funciones(montos[3])
		ciclo = str(input("Desea continuar?SI/NO: "))
		continuar = (ciclo == "SI")