class Usuario:

    nombre_table = "usuarios"

    def __init__(self, nombre, usuario, email):
        self.nombre = nombre
        self.apellido = ""
        self.usuario = usuario
        self.email = email
        self.ingresos = 0

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido} ({self.ingresos})"

    def login(self):
        self.ingresos += 1
        return self

    @staticmethod
    def crear_nombre():
        return "Nombre Nuevo"

    @classmethod
    def cambiar_nombre_tabla(cls, nombre_nuevo):
        cls.nombre_table = nombre_nuevo

    def __str__(self):
        return self.nombre_completo()


pancho = Usuario("Francisco", "fboisier", "fboisier@skillnest.com")
Usuario.cambiar_nombre_tabla("otra cosa")
pancho.apellido = "Boisier"
pancho.login()

print(pancho.nombre_table)
print(Usuario.nombre_table)

print(pancho.nombre_completo())

pancho.login()
print(str(pancho))

print(Usuario.crear_nombre())
