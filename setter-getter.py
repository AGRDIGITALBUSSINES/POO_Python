# class Millas:
#   def __init__(self, distance = 0):
#         self.distance = distancia
#
#   def convertir_a_kilometros(self):
#         return (self.distance * 1.609344)
#
#
#   # Creamos un nuevo objeto
#   avion = Millas()
#
#   # Indicamos la distancia
#   avion.distancia = 200
#
#   # Obtenemos el atributo distancia
#       print(avion.distancia)
#
#   # obtenemos el método convertir_a_kilometros
#     print(avion.convertir_a_kilometros())

# class Millas:
#     def __init__(self, distancia = 0):
#         self.distancia = distancia
#
#     def convertir_a_kilometros(self):
#         return (self.distance * 1.609344)
#
#     # Método getter
#     def obtener_distancia(self):
#         return self._distancia
#
#
#     # Método setter
#     def definir_distancia(self, valor):
#         if valor < 0:
#             raise ValueError("No es posible convertir distancias menores a 0.")
#         self._distancia = valor


# class Millas:
# 	def __init__(self):
# 		self._distancia = 0
#
# 	# Función para obtener el valor de _distancia
# 	def obtener_distancia(self):
# 		print("Llamada al método getter")
# 		return self._distancia
#
# 	# Función para definir el valor de _distancia
# 	def definir_distancia(self, recorrido):
# 		print("Llamada al método setter")
# 		self._distancia = recorrido
#
# 	# Función para eliminar el atributo _distancia
# 	def eliminar_distancia(self):
# 		del self._distancia
#
# 	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)
#
# # Creamos un nuevo objeto
# avion = Millas()
#
# # Indicamos la distancia
# avion.distancia = 200
#
# # Obtenemos su atributo distancia
# print(avion.distancia)

class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
    print(avion.definir.distancia)
