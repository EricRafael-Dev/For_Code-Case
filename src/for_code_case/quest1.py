import matplotlib.pyplot as plt
import numpy as np

def quest1(temp_F, constant_R=8.314, critical_temperature_Tc=304.2, critical_pressure_Pc=73.83e5):
    
    def to_kelvin(temp_F):
        return  ((temp_F-32)/1.8)+273.15
    
    def plotGraph(molar_volume, pressure):
        plt.plot(molar_volume, pressure)
        plt.xlabel('Molar Volume (m^3/mol)')
        plt.ylabel('Pressure (Pa)')
        plt.title('Pressure vs Molar Volume')
        plt.grid()
        plt.show()
        
    temp_K = to_kelvin(temp_F)
    
    a = (27/64)*((constant_R**2*critical_temperature_Tc**2)/critical_pressure_Pc)
    b = (1/8)*((constant_R*critical_temperature_Tc)/critical_pressure_Pc)
    molar_volume = np.linspace(b + 0.001, 0.1, 100)
    pressure = ((constant_R*temp_K)/molar_volume-b) - a/(molar_volume**2)


    return plotGraph(molar_volume, pressure)