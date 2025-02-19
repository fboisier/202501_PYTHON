class PermisoBase:

    aplicar_defecto = False
    is_ajax = False

    def __init__(self):
        self.permisosDefecto = 5

    def getAplicarDefecto(self):
        return self.aplicar_defecto


class PermisosA(PermisoBase):

    def get_permisosA(self):

        if self.getAplicarDefecto():
            return self.permisosDefecto
        return 0

    @staticmethod
    def saludar():
        return "Hola"

    def generarPaginaA(self):
        if self.is_ajax:
            return {"saludo": "Hola Alumnos"}

        return "<h1>Hola Alumnos</h1>"


class PermisosB(PermisoBase):

    def get_permisosB(self):
        if self.getAplicarDefecto():
            return self.permisosDefecto
        return 1

    @staticmethod
    def saludar():
        return "Chao"

    def generarPaginaB(self):
        if self.is_ajax:
            return {"saludo": "Chao Alumnos"}

        return "<h1>Chao Alumnos</h1>"


class AccesoAdmin(PermisosB, PermisosA):

    aplicar_defecto = True
    is_ajax = True

    def get_permiso(self):
        return self.get_permisosA() + self.get_permisosB()


instanciaAcceso = AccesoAdmin()

print(instanciaAcceso.get_permiso())
print(instanciaAcceso.saludar())
print(instanciaAcceso.generarPaginaA())


class AccesoAdminDos(PermisosB, PermisosA):

    aplicar_defecto = True
    is_ajax = False

    def get_permiso(self):
        return self.get_permisosA() + self.get_permisosB()

    def saludar(self):
        return "Hola Chao que tal" + str(self.is_ajax) + str(self.permisosDefecto)


instanciaAcceso2 = AccesoAdminDos()

print(instanciaAcceso2.get_permiso())
print(instanciaAcceso2.saludar())
print(instanciaAcceso2.generarPaginaA())
