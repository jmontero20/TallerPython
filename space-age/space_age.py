class SpaceAge:
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round((self.seconds/31557600), 2)

    def on_mercury(self):
        return round((self.seconds/7600543.81992), 2)

    def on_venus(self):
        return round((self.seconds/19414149.0522), 2)

    def on_mars(self):
        return round((self.seconds/59354032.6901), 2)

    def on_jupiter(self):
        return round((self.seconds/374355659.124), 2)

    def on_saturn(self):
        return round((self.seconds/929292362.885), 2)

    def on_uranus(self):
        return round((self.seconds/2651370019.33), 2)

    def on_neptune(self):
        return round((self.seconds/5200418560.03), 2)
