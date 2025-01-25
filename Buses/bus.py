class Bus:
    def __init__(self, bus_id):
        self.bus_id = bus_id
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            print(f"El horario {horario} ya está asignado al bus {self.bus_id}.")
    
    def asignar_conductor(self, conductor):
        self.conductor_asignado = conductor

