# Classes for actuators in functional RC-Models
from sensors import *

class Motor:
    """A class for all motor types"""
    def __init__(self,mode:int):
        self.modes=mode #Possible modes: 1=pwm control one direction,2=pwm control two direction, 3 rpm control
        self.has_MotorTemp=False
        self.has_ControllerTemp=False
        self.has_watercooling=False     
        self.requested_rpm:int=0
        self.measured_rpm:int=0
        self.min_rpm:int=0
        self.max_rpm:int=0
        self.voltage:float=0
        self.current:float=0
        self.stop_current:float=0
        self.pwm_value:int=0
        self.error_state:str="No error"
        self.pin_pwm_in:int=0
        self.pin_pwm_out:int=0
            
    def create_motor_temperature_sensor(self,sensortype,pin):
        """Creates a temperature sensor for the motor"""
        self.MotorTemp=TempSensor(sensortype,pin)
        # Take a first reading to check for valid results:
        self.MotorTemp.read_temp()
        self.has_MotorTemp=True
        self.max_motor_temp:float=60
        
    def create_controller_temperature_sensor(self,sensortype,pin):
        """Creates a temperature sensor for the controller."""
        self.ControllerTemp=TempSensor(sensortype,pin)
        # Take a first reading to check for valid results:
        self.ControllerTemp.read_temp()
        self.has_ControllerTemp=True
        self.max_controller_temp:float=80
        
    def set_rpm(self,rpm_in):
        """Method to set a target speed"""
        if rpm_in>self.min_rpm:
            if rpm_in<self.max_rpm:
                self.requested_rpm=rpm_in
                print("RPM set to "+str(rpm_in)+".")
            else:
                print("Requested RPM more than max_rpm!")
        else:
            print("Requested RPM below min_rpm!")
            
    def get_rpm(self)->float:
        """Method returns the actual speed."""
        return self.measured_rpm
                    
    def measure_rpm(self):
        """Method to measure the rpm from the measurement buffer"""
        # TO DO: Implement sensors and measurements!
        self.measured_rpm=200

class Valve:
    """A valve to control hydraulic systems."""
    pass

class Pump:
    """A class for a pump"""
    pass

class WaterCoolingSystem:
    """A water cooling system for any other system."""
    def __init__(self):
        #Example:
        self.watertemp_in:float=0
        self.watertemp_out:float=0
        self.waterpressure_in:float=0
        self.max_watertemp_in:float=30
        self.max_watertemp_out:float=60
        self.min_waterpressure_in:float=0.5
    pass

class FireFightingMonitor:
    """A fire fighting monitor with servos / gimbal, optional stabilisation"""
    pass

