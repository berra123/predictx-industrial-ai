import random


class ScenarioEngine:

    def __init__(self):

        self.running = False

        # Aktif senaryo
        self.scenario = "Normal"

        # Başlangıç değerleri
        self.current = 115
        self.temperature = 58
        self.vibration = 2.1
        self.torque = 401

    # -----------------------
    # Demo Controller
    # -----------------------

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):

        self.current = 115
        self.temperature = 58
        self.vibration = 2.1
        self.torque = 401

    def is_running(self):
        return self.running

    def set_scenario(self, scenario):
        self.scenario = scenario

    # -----------------------
    # Telemetry Generator
    # -----------------------

    def next(self):

        # Demo durmuşsa mevcut değerleri döndür
        if not self.running:

            return {
                "current": round(self.current, 1),
                "temperature": round(self.temperature, 1),
                "vibration": round(self.vibration, 2),
                "torque": round(self.torque, 1)
            }

        # =========================
        # NORMAL
        # =========================
        if self.scenario == "Normal":

            self.current += random.uniform(-1.5, 1.5)
            self.temperature += random.uniform(-0.6, 0.6)
            self.vibration += random.uniform(-0.12, 0.12)
            self.torque += random.uniform(-3, 3)

        # =========================
        # BEARING WEAR
        # =========================
        elif self.scenario == "Bearing Wear":

            self.current += random.uniform(0.5, 2.0)
            self.temperature += random.uniform(0.5, 1.2)
            self.vibration += random.uniform(0.15, 0.35)
            self.torque += random.uniform(1, 5)

        # =========================
        # OVERHEATING
        # =========================
        elif self.scenario == "Overheating":

            self.current += random.uniform(1.0, 3.0)
            self.temperature += random.uniform(1.5, 3.0)
            self.vibration += random.uniform(0.0, 0.15)
            self.torque += random.uniform(1, 4)

        # =========================
        # MOTOR FAILURE
        # =========================
        elif self.scenario == "Motor Failure":

            self.current += random.uniform(3.0, 5.0)
            self.temperature += random.uniform(2.5, 4.5)
            self.vibration += random.uniform(0.35, 0.65)
            self.torque += random.uniform(4, 8)

        # Güvenli limitler
        self.current = min(max(self.current, 105), 170)
        self.temperature = min(max(self.temperature, 50), 95)
        self.vibration = min(max(self.vibration, 1.5), 7.0)
        self.torque = min(max(self.torque, 380), 500)

        return {

            "current": round(self.current, 1),

            "temperature": round(self.temperature, 1),

            "vibration": round(self.vibration, 2),

            "torque": round(self.torque, 1)

        }


scenario = ScenarioEngine()