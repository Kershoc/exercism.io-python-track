class SpaceAge:
    earthYearInSeconds = 31557600
    mercury = 0.2408467
    venus = 0.61519726
    earth = 1
    mars = 1.8808158
    jupiter = 11.862615
    saturn = 29.447498
    uranus = 84.016846
    neptune = 164.79132
    pluto = 247.94

    def __init__(self, seconds):
        self.seconds = seconds
        pass

    def on_mercury(self):
        return round(self.seconds / self.earthYearInSeconds / self.mercury, 2)

    def on_venus(self):
        return round(self.seconds / self.earthYearInSeconds / self.venus, 2)

    def on_earth(self):
        return round(self.seconds / self.earthYearInSeconds / self.earth, 2)

    def on_mars(self):
        return round(self.seconds / self.earthYearInSeconds / self.mars, 2)

    def on_jupiter(self):
        return round(self.seconds / self.earthYearInSeconds / self.jupiter, 2)

    def on_saturn(self):
        return round(self.seconds / self.earthYearInSeconds / self.saturn, 2)

    def on_uranus(self):
        return round(self.seconds / self.earthYearInSeconds / self.uranus, 2)

    def on_neptune(self):
        return round(self.seconds / self.earthYearInSeconds / self.neptune, 2)

    def on_pluto(self):
        return round(self.seconds / self.earthYearInSeconds / self.pluto, 2)
