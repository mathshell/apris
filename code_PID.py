import time

#definisson la clase de notre regulateur PID
class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error_prev = 0
        self.integral = 0

    #calcul du PID
    def update(self, error):
        self.integral += error
        d_error = error - self.error_prev
        output = self.kp * error + self.ki * self.integral + self.kd * d_error

        self.error_prev = error
        return output

#Example usage
pid = PID(1.0, 0.1, 0.01)
while True:
    error = 1 # erreur retenu lor de la comparaison
    output = pid.update(error)
    # sortie.
    time.sleep(0.01)