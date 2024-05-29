
class Bluetooth:
    def __init__(self, sound, battery_level):
        self.sound = sound
        self.battery_level = battery_level
    
    def display_information(self):
        print("I am a Bluetooth devices with multiple responsibilities")
        print("Sound:", self.sound)
        print("Battery level:", self.battery_level)
    
class Speaker(Bluetooth):
    def __init__(self, sound, battery_level):
        super().__init__ (sound, battery_level)
    def display_information(self):
        print("The speaker is responsible for creating sound in the bluetooth")
        print("Speaker - sound:", self.sound)
        print("Speaker - battery level:", self.battery_level)


class Radio(Bluetooth):
    def __init__(self, sound, battery_level):
        super().__init__(sound, battery_level)
    def display_information(self):
        print("The radio is another features in the bluetooth for livestream of progammes in audio context")
        print("Radio - sound:", self.sound)
        print("Radio- battery level:", self.battery_level)
        

class Charger(Bluetooth):
    def __init__(self, sound, battery_level):
        super().__init__(sound, battery_level)
    def display_information(self):
        print("There is a USB ports provision made on the bluetooth device for charging of mobile phones")
        print("Charger - sound:", self.sound)
        print("Charger- battery level:", self.battery_level)
        

class Touch_light(Bluetooth):
    def __init__(self, sound, battery_level):
        super().__init__(sound, battery_level)
    def display_information(self):
        print("There is a touch light on the bluetooth device")
        print("Touch light - sound:", self.sound)
        print("Touch light- battery level:", self.battery_level)


bluetooth_device = Bluetooth("Stereo", "High")
bluetooth_device.display_information()

speaker = Speaker("Bass", "High")
speaker.display_information()

radio = Radio("FM", "Medium")
radio.display_information()

charge = Charger("Silent", "Full")
charge.display_information()

touch_light = Touch_light("Low", "Medium")
touch_light.display_information()
