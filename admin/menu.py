from Buses.bus import Bus
from Conductores.conductor import Conductor

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            
            case = input("Seleccione una opción: ")

            if case == "1":
                self.agregar_bus()
            elif case == "2":
                self.agregar_ruta_a_bus()
            elif case == "3":
                self.registrar_horario_a_bus()
            elif case == "4":
                self.agregar_conductor()
            elif case == "5":
                self.agregar_horario_a_conductor()
            elif case == "6":
                self.asignar_bus_a_conductor()
            elif case == "7":
                print("Saliendo...")
                break
            else:
                print("Opción no válida")

    def agregar_bus(self):
        bus_id = input("Ingrese el ID del bus: ")
        nuevo_bus = Bus(bus_id)
        self.buses.append(nuevo_bus)
        print(f"Bus con ID {bus_id} agregado exitosamente.")

    def agregar_ruta_a_bus(self):
        bus_id = input("Ingrese el ID del bus: ")
        ruta = input("Ingrese la ruta del bus: ")
        bus = self.obtener_bus_por_id(bus_id)
        if bus:
            bus.agregar_ruta(ruta)
            print(f"Ruta {ruta} agregada al bus {bus_id}.")
        else:
            print("Bus no encontrado.")

    def registrar_horario_a_bus(self):
        bus_id = input("Ingrese el ID del bus: ")
        horario = input("Ingrese el horario del bus (hora): ")
        bus = self.obtener_bus_por_id(bus_id)
        if bus:
            bus.registrar_horario(horario)
            print(f"Horario {horario} agregado al bus {bus_id}.")
        else:
            print("Bus no encontrado.")

    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        nuevo_conductor = Conductor(nombre)
        self.conductores.append(nuevo_conductor)
        print(f"Conductor {nombre} agregado exitosamente.")

    def agregar_horario_a_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        horario = input("Ingrese el horario del conductor (hora): ")
        conductor = self.obtener_conductor_por_nombre(nombre)
        if conductor:
            if conductor.agregar_horario(horario):
                print(f"Horario {horario} agregado al conductor {nombre}.")
            else:
                print(f"El conductor {nombre} ya tiene un horario a las {horario}.")
        else:
            print("Conductor no encontrado.")

    def asignar_bus_a_conductor(self):
        bus_id = input("Ingrese el ID del bus: ")
        nombre_conductor = input("Ingrese el nombre del conductor: ")
        
        bus = self.obtener_bus_por_id(bus_id)
        conductor = self.obtener_conductor_por_nombre(nombre_conductor)
        
        if bus and conductor:
            if conductor.asignar_bus(bus):
                print(f"Bus {bus_id} asignado al conductor {nombre_conductor}.")
            else:
                print(f"El conductor {nombre_conductor} ya tiene un bus asignado a ese horario.")
        else:
            print("Bus o conductor no encontrados.")

    def obtener_bus_por_id(self, bus_id):
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
        return None

    def obtener_conductor_por_nombre(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None
