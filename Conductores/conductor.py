class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []
        self.bus_asignado = None

    def agregar_horario(self, horario):
        if horario in self.horarios:
            return False  
        self.horarios.append(horario)
        return True

    def asignar_bus(self, bus):
        if self.bus_asignado is not None:
            return False  
        self.bus_asignado = bus
        bus.asignar_conductor(self)
        return True
