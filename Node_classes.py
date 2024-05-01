# Classes for Systems in functional RC Models
from actuators import *
        
class Propulsion:
    """A class for a propulsion system, e.g. Controller, Motor, Sensors and water cooling system"""
    pass

class FireFightingSystem:
    """A class for a fire fighting system, consisting e.g. of a pump, valves and a fire fighting monitor."""
    pass

class AnchorWinch:
    """A modular class for anchor winches, with chain brake, winch motor etc."""
    pass

class GeneralWinch:
    """A class for all other winches on deck, consisting e.g. of motor, sensors, and encoder"""
    pass

class NavigationSignals:
    """This class manages all navigation lights and shapes"""
    pass

class ShipSafetySystem:
    """This class handles water ingress detection, bilge pumps and emergency signals."""
    pass

    
        
# debugging:
if __name__=='__main__':
    print('Start debugging mode')
    andimot=Motor(2)
    print(andimot.modes)
    andimot.min_rpm=10
    andimot.max_rpm=3500
    andimot.set_rpm(300)
    andimot.measure_rpm()
    rpm=andimot.get_rpm()
    print("RPM="+str(rpm))
    andimot.create_motor_temperature_sensor(1,10)
    tmp=andimot.MotorTemp.get_temp()
    print("Motor temperature: "+str(tmp))
    andimot.create_controller_temperature_sensor(1,11)
    tmp=andimot.ControllerTemp.get_temp()
    print("Controller temperature: "+str(tmp))
    
    