#  create a test tv program

class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    
    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False
    
    def getChannel(self):
        return self.channel
    
    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
    
    def getVolume(self):
        return self.volumeLevel
    
    def setVolumeLevel(self, volumeLevel):
        if 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    
    def channelUp(self):
        if self.channel < 120:
            self.channel += 1
    
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
    
    def volumeUp(self):
        if self.volumeLevel < 7:
            self.volumeLevel += 1
    
    def volumeDown(self):
        if self.volumeLevel > 1:
            self.volumeLevel -= 1

def TestTV():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolumeLevel(3)
    
    tv2 = TV()
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolumeLevel(2)
    
    print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

TestTV()
