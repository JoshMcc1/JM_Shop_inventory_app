class Product:
    def __init__(
        self,
        name,
        description,
        stock_quantity,
        buying_cost,
        selling_cost,
        manufacturer,
        horse_power,
        top_speed,
        type,
        id=None,
    ):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.manufacturer = manufacturer
        self.horse_power = horse_power
        self.top_speed = top_speed
        self.type = type
        self.id = id

    def calculate_markup(self):
        return self.selling_cost - self.buying_cost
