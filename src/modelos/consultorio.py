from datetime import date
from typing import Optional

from src.estructuras.pila_urgencias import PilaUrgencias
from src.modelos.cita import Cita
from src.modelos.tipo_atencion import TipoAtencion

class Consultorio:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita: Cita):
        self.citas.append(cita)

    def total_clientes(self) -> int:
        return len(self.citas)

    def ingresos_totales(self) -> int:
        total = 0
        for cita in self.citas:
            total += cita.valor_total_cita()
        return total

    def cantidad_extracciones(self) -> int:
        contador = 0
        for cita in self.citas:
            if cita.tipo_atencion == TipoAtencion.EXTRACCION:
                contador += 1
        return contador

    def ordenar_por_valor_descendente(self):
        n = len(self.citas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.citas[j].valor_total_cita() < self.citas[j+1].valor_total_cita():
                    self.citas[j], self.citas[j+1] = self.citas[j+1], self.citas[j]

    def buscar_por_cedula(self, cedula: int) -> Cita:
        for cita in self.citas:
            if cita.cliente.cedula == cedula:
                return cita
        return None

    def crear_pila_urgencias(self) -> PilaUrgencias:
        return PilaUrgencias(self.citas)