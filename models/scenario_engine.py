class ScenarioEngine:

    def __init__(self):

        self.index = 0
        self.running = False

        self.scenario = [

            {
                "current": 115,
                "temperature": 58,
                "vibration": 2.1,
                "torque": 401
            },

            {
                "current": 116,
                "temperature": 59,
                "vibration": 2.2,
                "torque": 403
            },

            {
                "current": 117,
                "temperature": 60,
                "vibration": 2.4,
                "torque": 406
            },

            {
                "current": 118,
                "temperature": 61,
                "vibration": 2.7,
                "torque": 409
            },

            {
                "current": 119,
                "temperature": 63,
                "vibration": 3.0,
                "torque": 415
            },

            {
                "current": 121,
                "temperature": 65,
                "vibration": 3.4,
                "torque": 420
            },

            {
                "current": 123,
                "temperature": 67,
                "vibration": 3.8,
                "torque": 426
            }

        ]

    def next(self):

        data = self.scenario[self.index]

        if self.running:

            self.index += 1

            if self.index >= len(self.scenario):
                self.index = 0

        return data

    def start(self):

        self.running = True

    def pause(self):

        self.running = False

    def is_running(self):

        return self.running

    def reset(self):

        self.index = 0
        self.running = False


scenario = ScenarioEngine()