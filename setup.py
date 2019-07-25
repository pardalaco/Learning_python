from setuptools import setup

setup(#Esto sirve para dar una descripcion al paquete

	name="paquetecalculos",
	version="1.0",
	descripcion="Paquete de recondeo y potencioas",
	autor="Daniel Rovira",
	autor_email="pardalaco@gmail.com",
	url="http://holusoydani.com",
	packages=["calculos", "calculos.recondeo_potencia"]#Esto es para localizar el subpaquete


	)