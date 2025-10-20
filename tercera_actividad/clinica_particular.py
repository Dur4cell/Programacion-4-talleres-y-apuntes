from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

class Persona:
    """Clase base simple para personas"""
    def __init__(self, nombre: str, edad: int, dni: str):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def __str__(self) -> str:
        return f"{self.nombre} (DNI: {self.dni})"

class Paciente(Persona):
    """Paciente con una lista de historias clínicas"""
    def __init__(self, nombre: str, edad: int, dni: str):
        super().__init__(nombre, edad, dni)
        self.historias: List['HistoriaClinica'] = []

    def quejarse(self) -> str:
        return "¡Me siento mal!"

    def agregar_historia(self, historia: 'HistoriaClinica') -> None:
        self.historias.append(historia)

    def obtener_historia_actual(self) -> Optional['HistoriaClinica']:
        if not self.historias:
            return None
        return self.historias[-1]

class Doctor(Persona):
    """Doctor con especialidad y métodos para crear registros"""
    def __init__(self, nombre: str, edad: int, dni: str, especialidad: str):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad

    def diagnosticar(self) -> str:
        return "Después de examinarte, te recetaré un acetaminofén."

    def crear_historia_clinica(self, paciente: Paciente) -> 'HistoriaClinica':
        return HistoriaClinica(paciente, self)

class HistoriaClinica:
    """Colección de registros médicos asociada a un paciente"""
    def __init__(self, paciente: Paciente, doctor_responsable: Doctor):
        self.id = f"HC-{int(datetime.now().timestamp())}"
        self.paciente = paciente
        self.doctor_responsable = doctor_responsable
        self.fecha_creacion = datetime.now()
        self.activa = True
        self.registros: List[dict] = []
        paciente.agregar_historia(self)

    def agregar_registro(self, doctor: Doctor, diagnostico: str, tratamiento: str, observaciones: str = "") -> None:
        registro = {
            "fecha": datetime.now(),
            "doctor": doctor,
            "diagnostico": diagnostico,
            "tratamiento": tratamiento,
            "observaciones": observaciones
        }
        self.registros.append(registro)

    def obtener_registros(self) -> List[dict]:
        return list(self.registros)

    def __str__(self) -> str:
        estado = "ACTIVA" if self.activa else "INACTIVA"
        return f"Historia {self.id} - Paciente: {self.paciente.nombre} - {estado}"

class SistemaClinica:
    """Gestor sencillo de pacientes, doctores e historias"""
    def __init__(self):
        self.pacientes: List[Paciente] = []
        self.doctores: List[Doctor] = []
        self.historias: List[HistoriaClinica] = []

    def registrar_paciente(self, nombre: str, edad: int, dni: str) -> Paciente:
        paciente = Paciente(nombre, edad, dni)
        self.pacientes.append(paciente)
        return paciente

    def registrar_doctor(self, nombre: str, edad: int, dni: str, especialidad: str) -> Doctor:
        doctor = Doctor(nombre, edad, dni, especialidad)
        self.doctores.append(doctor)
        return doctor

    def crear_historia_clinica(self, paciente: Paciente, doctor: Doctor) -> HistoriaClinica:
        historia = doctor.crear_historia_clinica(paciente)
        self.historias.append(historia)
        return historia

    def agregar_registro_historia(self, historia: HistoriaClinica, doctor: Doctor, diagnostico: str, tratamiento: str, observaciones: str = "") -> None:
        historia.agregar_registro(doctor, diagnostico, tratamiento, observaciones)

    def obtener_historias_paciente(self, paciente: Paciente) -> List[HistoriaClinica]:
        return paciente.historias

if __name__ == "__main__":
    # Ejemplo mínimo de uso
    sistema = SistemaClinica()

    dr_garcia = sistema.registrar_doctor("Carlos García", 45, "12345678", "Cardiología")
    paciente = sistema.registrar_paciente("María López", 37, "87654321")

    hc = sistema.crear_historia_clinica(paciente, dr_garcia)
    sistema.agregar_registro_historia(hc, dr_garcia, "Hipertensión", "Losartán 50mg/día", "Control inicial")

    print("Doctores:", len(sistema.doctores))
    print("Pacientes:", len(sistema.pacientes))
    print("Historias:", len(sistema.historias))
    for r in hc.obtener_registros():
        print(f"- {r['fecha']:%Y-%m-%d %H:%M} | Dr. {r['doctor'].nombre}: {r['diagnostico']} -> {r['tratamiento']}")