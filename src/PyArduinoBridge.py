from enum import Enum 
import subprocess

class arduino_operations(Enum):
    SET_PIN_MODE = 0
    WRITE_GPIO = 1
    READ_GPIO  =  2
    READ_SPI = 3
    WRITE_SPI = 4
    READ_I2C = 5
    WRITE_I2C = 6


class arduino_cli:
    def __init__(self,cli_path="arduino-cli2"):
        self.cli_version = None
        try:
            self.cli_version = subprocess.run([cli_path])
        except OSError as error:
            print("Unable to find the arduino command line interface at path: %s" % cli_path) 
            raise error 
        

if __name__=='__main__':
    arduino_cli()
        
    