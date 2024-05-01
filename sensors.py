"""Classes for Sensors in functional RC Models."""
class TempSensor:
    """A Class for all kinds of temperature sensors."""
    def __init__(self,sensortype:int,pin:int):
        self.adress:str=''
        self.sensor_type=sensortype #Define possible sensor types
        self.measure_pin=pin # Pin with actual connection to sensor
        self.temperature:float=0
        self.error_state:str='No error.'
        
    def read_temp(self):
        """Reads a temperature value and stores it."""
        # TO DO: Implement sensor reading based on sensor type etc.
        self.temperature=20
        
    def get_temp(self)->float:
        """Returns the measured temperature."""
        return self.temperature
  
class RPMSensor:
    """A Class for all kinds of rpm sensors."""
    def __init__(self):
        self.adress:str=''
        self.sensor_type:int=0
        self.measure_pin:int=0
        self.impulses_per_rotation:int=1
        self.rpm:float=0
        self.error_state:str='No error.'
        
    def measure_rpm(self):
        """Takes a reading and stores the value"""
        #TO DO: Implement actual reading
        self.rpm=400
        
    def get_rpm(self)->float:
        """Returns the actual RPM."""
        return self.rpm

class PressureSensor:
    """A Class for all kinds of pressure sensors."""
    def __init__(self):
        self.adress:str=''
        self.sensor_type:int=0
        self.measure_pin:int=0
        self.pressure:float=0
        self.error_state:str='No error.'
        
    def read_pressure(self):
        """Reads a pressure value and stores it."""
        # TO DO: Implement sensor reading based on sensor type etc.
        self.pressure=2
        
    def get_pressure(self)->float:
        """Returns the measured pressure."""
        return self.pressure

class PowerMeter:
    """A class for voltage and current measurements."""
    def __init__(self):
        self.voltage:float=0
        self.current:float=0
        self.power:float=0
        
    def measure(self):
        """Take actual reading and store variables"""
        self.voltage=13.1 #Volts
        self.current=2.4  #Amps
        self.power=self.voltage*self.current #Watt
        
    def get_voltage(self)->float:
        """Return voltage reading [Volts]"""
        return self.voltage
    
    def get_current(self)->float:
        """Return current reading [Amps]"""
        return self.current
    
    def get_power(self)->float:
        """Return power reading [Watt]"""
        return self.power

class WaterSensor:
    """A class for a water detection or water level measurement sensor."""
    pass

class BrightnessSensor:
    """A sensor to measure ambient brightness, to trigger navigation lights."""
    pass

if __name__=="__main__":
    CoolingWaterSensor=TempSensor
    pass
