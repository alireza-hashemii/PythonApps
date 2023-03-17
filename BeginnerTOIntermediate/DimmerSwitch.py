class DimmerSwitch:
    def __init__(self):
        self.IsOn = False
        self.IsMute = False
        self.MaximumVolume = 10
        self.volume = 0

    def turn_on(self):
        self.IsOn = True
        return None
    
    def raise_volume(self):
        if self.IsOn == False:
            print("it's not on")
            return None
        
        elif self.IsMute == True:
            self.IsMute = not self.IsMute
            if self.volume < self.MaximumVolume:
                self.volume += 1
                print("Done")

        elif self.volume < self.MaximumVolume:
            self.volume += 1
            return None
        else:
            print("It's not possible")

    def reduce_volume(self):
        if self.volume < 1:
            print("lowest volume")
            return None
        else:
            self.volume -= 1
            return None

        
odimmer = DimmerSwitch()
odimmer.IsOn = True
odimmer.raise_volume()
print(odimmer.volume)
odimmer.reduce_volume()
odimmer.reduce_volume()
odimmer.reduce_volume()
odimmer.reduce_volume()
odimmer.reduce_volume()
odimmer.reduce_volume()
print(odimmer.volume)


