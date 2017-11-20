import math as m
from utils import Polynomial


class Battery:
    # capacity in Ah
    def __init__(self, total_capacity, R0, R1, C1):
        # capacity in As
        self.total_capacity = total_capacity * 3600
        self.actual_capacity = self.total_capacity

        # Thevenin model : OCV + R0 + R1//C1
        self.R0 = R0
        self.R1 = R1
        self.C1 = C1

        self._current = 0
        self._RC_voltage = 0

        # polynomial representation of OCV vs SoC
        self._OCV_model = Polynomial([3.1400, 3.9905, -14.2391, 24.4140, -13.5688, -4.0621, 4.5056])

    def update(self, time_delta):
        self.actual_capacity -= self.current * time_delta
        exp_coeff = m.exp(-time_delta/(self.R1*self.C1))
        self._RC_voltage *= exp_coeff
        self._RC_voltage += self.R1*(1-exp_coeff)*self.current
    
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, current):
        self._current = current

    @property
    def voltage(self):
        return self.OCV - self.R0 * self.current - self._RC_voltage

    @property
    def state_of_charge(self):
        return self.actual_capacity/self.total_capacity

    @property
    def OCV_model(self):
        return self._OCV_model

    @property
    def OCV(self):
        return self.OCV_model(self.state_of_charge)


if __name__ == '__main__':
    capacity = 3.2 #Ah
    discharge_rate = 1 #C
    time_step = 10 #s
    cut_off_voltage = 2.5


    current = capacity*discharge_rate
    my_battery = Battery(capacity, 0.062, 0.01, 3000)
    my_battery.current = current
    
    time = [0]
    SoC = [my_battery.state_of_charge]
    OCV = [my_battery.OCV]
    RC_voltage = [my_battery._RC_voltage]
    voltage = [my_battery.voltage]
    
    while my_battery.voltage>cut_off_voltage:
        my_battery.update(time_step)
        time.append(time[-1]+time_step)
        SoC.append(my_battery.state_of_charge)
        OCV.append(my_battery.OCV)
        RC_voltage.append(my_battery._RC_voltage)
        voltage.append(my_battery.voltage)
        # print(time[-1], my_battery.state_of_charge, my_battery._OCV, my_battery.voltage)

    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # title, labels
    ax1.set_title('')    
    ax1.set_xlabel('SoC')
    ax1.set_ylabel('Voltage')

    ax1.plot(SoC, OCV, label="OCV")
    ax1.plot(SoC, voltage, label="Total voltage")

    plt.show()


