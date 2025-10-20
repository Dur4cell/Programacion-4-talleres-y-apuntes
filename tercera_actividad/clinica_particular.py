class Persona:
    def __init__(self,nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

class Paciente(Persona):
    def __init__(self, nombre, edad, dni, reg_historia_clinica):
        super().__init__(nombre, edad, dni)
        self.__reg_historia_clinica = reg_historia_clinica     

    def quejarse(self):
        return "¡Me siento mal!"
    
class Doctor(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.__especialidad = especialidad

    def diagnosticar(self):
        return "Después de examinarte, te recetaré un acetaminofén."
    def crear_historia_clinica(self, paciente, historia):
        pass
    
class historia_clinica:
    def __init__(self):
        self.__registros = []

    def agregar_registro(self, registro):
        self.__registros.append(registro)

    def obtener_registros(self):
        return self.__registros

""""
   
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
import uuid

class Persona(ABC):
    """Clase abstracta base para todas las personas del sistema"""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
    
    @abstractmethod
    def obtener_info_completa(self) -> str:
        pass
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Paciente(Persona):
    """Representa a un paciente de la clínica"""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, telefono: str, 
                 fecha_nacimiento: datetime, direccion: str):
        super().__init__(id, nombre, apellido, email, telefono)
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.historias_clinicas: List['HistoriaClinica'] = []
        self.activo = True
    
    def agregar_historia_clinica(self, historia: 'HistoriaClinica'):
        """Agrega una nueva historia clínica al paciente"""
        self.historias_clinicas.append(historia)
    
    def obtener_historia_actual(self) -> Optional['HistoriaClinica']:
        """Obtiene la historia clínica activa más reciente"""
        if not self.historias_clinicas:
            return None
        return max(self.historias_clinicas, key=lambda h: h.fecha_creacion)
    
    def obtener_info_completa(self) -> str:
        info = f"PACIENTE: {self.nombre} {self.apellido}\n"
        info += f"ID: {self.id} | Email: {self.email} | Tel: {self.telefono}\n"
        info += f"Fecha Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}\n"
        info += f"Dirección: {self.direccion}\n"
        info += f"Historias Clínicas: {len(self.historias_clinicas)}"
        return info

class Doctor(Persona):
    """Representa a un doctor de la clínica"""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, telefono: str,
                 especialidad: str, licencia: str):
        super().__init__(id, nombre, apellido, email, telefono)
        self.especialidad = especialidad
        self.licencia = licencia
        self.activo = True
    
    def obtener_info_completa(self) -> str:
        info = f"DOCTOR: {self.nombre} {self.apellido}\n"
        info += f"Especialidad: {self.especialidad} | Licencia: {self.licencia}\n"
        info += f"Email: {self.email} | Tel: {self.telefono}"
        return info

class RegistroMedico:
    """Representa un registro individual en la historia clínica"""
    
    def __init__(self, doctor: Doctor, diagnostico: str, tratamiento: str, 
                 observaciones: str = ""):
        self.id = str(uuid.uuid4())[:8]
        self.fecha = datetime.now()
        self.doctor = doctor
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
    
    def __str__(self) -> str:
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] Dr. {self.doctor.apellido}: {self.diagnostico}"

class HistoriaClinica:
    """Representa la historia clínica completa de un paciente"""
    
    def __init__(self, id: str, paciente: Paciente, doctor_responsable: Doctor):
        self.id = id
        self.paciente = paciente
        self.doctor_responsable = doctor_responsable
        self.fecha_creacion = datetime.now()
        self.activa = True
        self.registros: List[RegistroMedico] = []
        
        # Relación bidireccional
        paciente.agregar_historia_clinica(self)
    
    def agregar_registro(self, doctor: Doctor, diagnostico: str, tratamiento: str, 
                        observaciones: str = "") -> RegistroMedico:
        """Agrega un nuevo registro médico a la historia"""
        registro = RegistroMedico(doctor, diagnostico, tratamiento, observaciones)
        self.registros.append(registro)
        return registro
    
    def modificar_ultimo_registro(self, nuevo_diagnostico: str = None, 
                                 nuevo_tratamiento: str = None, 
                                 nuevas_observaciones: str = None) -> bool:
        """Modifica el último registro médico (solo si es del mismo día)"""
        if not self.registros:
            return False
        
        ultimo_registro = self.registros[-1]
        hoy = datetime.now().date()
        
        if ultimo_registro.fecha.date() == hoy:
            if nuevo_diagnostico:
                ultimo_registro.diagnostico = nuevo_diagnostico
            if nuevo_tratamiento:
                ultimo_registro.tratamiento = nuevo_tratamiento
            if nuevas_observaciones:
                ultimo_registro.observaciones = nuevas_observaciones
            return True
        return False
    
    def desactivar(self) -> None:
        """Desactiva la historia clínica (eliminación lógica)"""
        self.activa = False
    
    def obtener_registros_recientes(self, dias: int = 30) -> List[RegistroMedico]:
        """Obtiene registros de los últimos N días"""
        fecha_limite = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        from datetime import timedelta
        fecha_limite -= timedelta(days=dias)
        
        return [r for r in self.registros if r.fecha >= fecha_limite]
    
    def __str__(self) -> str:
        estado = "ACTIVA" if self.activa else "INACTIVA"
        return f"Historia Clínica {self.id} - Paciente: {self.paciente} - {estado}"


#def ejemplo_uso():
    """Ejemplo práctico de uso del sistema"""
    
    # Crear sistema
    sistema = SistemaGestionClinica()
    
    # Registrar doctores
    dr_garcia = sistema.registrar_doctor(
        "Carlos", "García", "c.garcia@clinica.com", "555-0101",
        "Cardiología", "LIC-12345"
    )
    
    dra_fernandez = sistema.registrar_doctor(
        "Ana", "Fernández", "a.fernandez@clinica.com", "555-0102",
        "Pediatría", "LIC-67890"
    )
    
    # Registrar pacientes
    paciente1 = sistema.registrar_paciente(
        "María", "López", "maria.lopez@email.com", "555-0201",
        datetime(1985, 5, 15), "Calle Principal 123"
    )
    
    paciente2 = sistema.registrar_paciente(
        "Juan", "Martínez", "juan.martinez@email.com", "555-0202",
        datetime(1990, 8, 22), "Avenida Central 456"
    )
    
    # Crear historias clínicas
    hc1 = sistema.crear_historia_clinica(paciente1, dr_garcia)
    hc2 = sistema.crear_historia_clinica(paciente2, dra_fernandez)
    
    # Agregar registros médicos
    sistema.agregar_registro_historia(
        hc1.id, dr_garcia,
        "Hipertensión arterial controlada",
        "Losartán 50mg 1 vez al día",
        "Presión arterial: 120/80 mmHg"
    )
    
    sistema.agregar_registro_historia(
        hc2.id, dra_fernandez,
        "Control pediátrico rutinario",
        "Vacuna influenza estacional",
        "Peso: 15kg, Talla: 95cm - Desarrollo normal"
    )
    
    # Mostrar información
    print("=== SISTEMA DE HISTORIAS CLÍNICAS ===")
    print(f"Doctores registrados: {len(sistema.doctores)}")
    print(f"Pacientes registrados: {len(sistema.pacientes)}")
    print(f"Historias clínicas: {len(sistema.historias_clinicas)}")
    
    print("\n=== HISTORIA CLÍNICA PACIENTE 1 ===")
    historia_paciente1 = sistema.obtener_historias_paciente(paciente1.id)[0]
    for registro in historia_paciente1.registros:
        print(f"- {registro}")

if __name__ == "__main__":
    ejemplo_uso()

"""