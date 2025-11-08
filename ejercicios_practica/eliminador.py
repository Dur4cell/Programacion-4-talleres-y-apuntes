class Texto:
    def __init__(self, contenido):
        self.contenido = contenido
    def __add__(self, other):
        # Elimina la subcadena de self.contenido que coincide con other.contenido
        return self.contenido + other.contenido

t1=Texto("esto es") 
t2=Texto(" " \
"una prueba")
print(t1+t2)