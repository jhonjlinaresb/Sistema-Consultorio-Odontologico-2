class EstructuraVaciaError(Exception):

    def __init__(self, mensaje: str = "La estructura no contiene elementos.") -> None:
        self.mensaje = mensaje
        super().__init__(self.mensaje)