import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class SistemaDifuso:
    def __init__(self):
        # Definición de variables
        #cambios en los limites min y max

        self.temperatura = ctrl.Antecedent(np.arange(34, 43, 0.1), 'temperatura')
        self.frecuencia_cardiaca = ctrl.Antecedent(np.arange(50, 131, 1), 'frecuencia_cardiaca')
        self.presion_arterial = ctrl.Antecedent(np.arange(80, 181, 1), 'presion_arterial')
        self.nivel_oxigeno = ctrl.Antecedent(np.arange(90, 102, 1), 'nivel_oxigeno')
        self.diagnostico = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'diagnostico')

        self._configurar_funciones_pertenencia()
        self._configurar_reglas()
        self._crear_sistema()

    def _configurar_funciones_pertenencia(self):
        # Configuración de funciones de pertenencia
        self.temperatura['baja'] = fuzz.trapmf(self.temperatura.universe, [34, 34, 36.5, 37])
        self.temperatura['normal'] = fuzz.trimf(self.temperatura.universe, [36.5, 37, 37.5])
        self.temperatura['alta'] = fuzz.trimf(self.temperatura.universe, [37, 38, 39])
        self.temperatura['muy_alta'] = fuzz.trapmf(self.temperatura.universe, [38, 39, 43, 43])

        self.frecuencia_cardiaca['baja'] = fuzz.trapmf(self.frecuencia_cardiaca.universe, [49, 49, 60, 70])
        self.frecuencia_cardiaca['normal'] = fuzz.trimf(self.frecuencia_cardiaca.universe, [60, 75, 90])
        self.frecuencia_cardiaca['alta'] = fuzz.trapmf(self.frecuencia_cardiaca.universe, [80, 100, 131, 131])

        self.presion_arterial['baja'] = fuzz.trapmf(self.presion_arterial.universe, [79, 79, 90, 100])
        self.presion_arterial['normal'] = fuzz.trimf(self.presion_arterial.universe, [90, 120, 140])
        self.presion_arterial['alta'] = fuzz.trapmf(self.presion_arterial.universe, [130, 150, 181, 181])

        self.nivel_oxigeno['bajo'] = fuzz.trapmf(self.nivel_oxigeno.universe, [89, 89, 93, 95])
        self.nivel_oxigeno['normal'] = fuzz.trimf(self.nivel_oxigeno.universe, [94, 96, 98])
        self.nivel_oxigeno['alto'] = fuzz.trapmf(self.nivel_oxigeno.universe, [97, 99, 101, 101])

        self.diagnostico['estable'] = fuzz.trapmf(self.diagnostico.universe, [0, 0, 0.2, 0.4])
        self.diagnostico['observacion'] = fuzz.trimf(self.diagnostico.universe, [0.3, 0.5, 0.7])
        self.diagnostico['alta_probabilidad_infeccion'] = fuzz.trapmf(self.diagnostico.universe, [0.6, 0.8, 1.1, 1.1])

    def _configurar_reglas(self):
        # Configuración de reglas
        regla1 = ctrl.Rule(self.temperatura['alta'] & self.nivel_oxigeno['bajo'], self.diagnostico['alta_probabilidad_infeccion'])
        regla2 = ctrl.Rule(self.temperatura['muy_alta'], self.diagnostico['alta_probabilidad_infeccion'])
        regla3 = ctrl.Rule(self.presion_arterial['alta'] & self.frecuencia_cardiaca['alta'], self.diagnostico['observacion'])
        regla4 = ctrl.Rule(self.frecuencia_cardiaca['normal'] & self.nivel_oxigeno['normal'], self.diagnostico['estable'])
        self.reglas = [regla1, regla2, regla3, regla4]

    def _crear_sistema(self):
        self.sistema_ctrl = ctrl.ControlSystem(self.reglas)
        self.sistema_simulacion = ctrl.ControlSystemSimulation(self.sistema_ctrl)

    def diagnosticar(self, entradas):
        """
        Realiza el diagnóstico basado en las entradas.
        :param entradas: Diccionario con las entradas del usuario.
        :return: Resultado del diagnóstico.
        """
        try:
            # Validar entradas dentro de los rangos definidos
            for key, value in entradas.items():
                if key not in ['temperatura', 'frecuencia_cardiaca', 'presion_arterial', 'nivel_oxigeno']:
                    raise KeyError(f"Entrada desconocida: {key}")
                if not (self.__dict__[key].universe.min() <= value <= self.__dict__[key].universe.max()):
                    raise ValueError(f"El valor para {key} ({value}) está fuera del rango permitido.")

                # Configurar la entrada
                self.sistema_simulacion.input[key] = value

            # Computar el diagnóstico
            self.sistema_simulacion.compute()

            # Validar si el diagnóstico fue calculado correctamente
            if 'diagnostico' in self.sistema_simulacion.output:
                return self.sistema_simulacion.output['diagnostico']
            else:
                raise KeyError("El sistema difuso no generó un diagnóstico válido. Verifique las reglas.")

        except Exception as e:
            print(f"Error en el cálculo del diagnóstico: {e}")
            return None
