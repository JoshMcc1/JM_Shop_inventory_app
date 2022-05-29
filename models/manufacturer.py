class Manufacturer:
    def __init__(self, name, country_of_origin, operating_status, id=None):
        self.name = name
        self.country_of_origin = country_of_origin
        self.operating_status = operating_status
        self.id = id

    def set_operating_status_false(self):
        self.operating_status = False

    def set_operating_status_true(self):
        self.operating_status = True
