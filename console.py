from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

product_repository.delete_all_products()
manufacturer_repository.delete_all_manufacturers()

manufacturer_1 = Manufacturer("Bugatti", "France", True)
manufacturer_repository.save_manufacturer(manufacturer_1)

manufacturer_2 = Manufacturer("Ferrari", "Italy", True)
manufacturer_repository.save_manufacturer(manufacturer_2)

manufacturer_3 = Manufacturer("Ford", "United States of America", True)
manufacturer_repository.save_manufacturer(manufacturer_3)

manufacturer_4 = Manufacturer("Astin Martin", "United Kingdom", True)
manufacturer_repository.save_manufacturer(manufacturer_4)

manufacturer_5 = Manufacturer("Honda", "Japan", True)
manufacturer_repository.save_manufacturer(manufacturer_5)


product_1 = Product(
    "Veyron",
    "TThe development of the BUGATTI VEYRON was one of the greatest technological challenges ever known in the automotive industry.",
    10,
    400000.00,
    12000000.00,
    manufacturer_1,
    1000,
    260,
    "Car",
)
product_repository.save_product(product_1)

product_2 = Product(
    "Chiron",
    "The Chiron is the fastest, most powerful, and exclusive production super sports car in Bugatti's history. Its sophisticated design, innovative technology, and iconic, performance-oriented form make it a unique masterpiece of art, form and technique, that pushes boundaries beyond imagination.",
    6,
    700000.00,
    18500000.00,
    manufacturer_1,
    1400,
    280,
    "Car",
)
product_repository.save_product(product_2)

product_3 = Product(
    "Transit",
    "Just name the task and there’s a Transit Van built for it. Transit Van comes with a single row of seats to maximise your load space and up to a capacious L4 H3 format And with the new 5-Tonne model, you can up the carrying strength of your Transit Van to 2,457 kg",
    20,
    15500.00,
    50000.00,
    manufacturer_3,
    450,
    150,
    "Van",
)
product_repository.save_product(product_3)

product_4 = Product(
    "Focus",
    "With a striking new design, and packed with next-gen connectivity, the New Focus experience is better than ever.",
    10,
    8000.00,
    22000.00,
    manufacturer_3,
    290,
    160,
    "Car",
)
product_repository.save_product(product_4)

product_5 = Product(
    "CBR650R",
    "The CBR650R has honed its racetrack DNA for aggressive road performance. The footpegs and handlebars give you the optimal riding position, for fluid movement around the machine, finding the perfect cornering balance as you tackle thrilling roads.",
    10,
    2000.00,
    14000.00,
    manufacturer_5,
    400,
    200,
    "Motorbike",
)
product_repository.save_product(product_5)

product_6 = Product(
    "HR-V",
    "Our HR-V is a full hybrid and, unlike a mild hybrid, delivers dynamic electrified performance for a new generation of eco-conscious drivers.",
    6,
    8000.00,
    32000.00,
    manufacturer_5,
    380,
    180,
    "SUV",
)
product_repository.save_product(product_6)

product_7 = Product(
    "296 GTB",
    "e 296 GTB, an evolution of Ferrari’s mid-rear-engined two-seater sports berlinetta concept, represents a revolution for the Maranello-based company as it introduces the new 120° V6 engine coupled with a plug-in (PHEV) electric motor capable of delivering up to 830 cv. The car thus defines the idea of driving fun to provide pure excitement not only when pursuing maximum performance but also in everyday driving.",
    4,
    250000.00,
    925000.00,
    manufacturer_2,
    750,
    220,
    "Car",
)
product_repository.save_product(product_7)

product_8 = Product(
    "SF90 SPIDER",
    "As the Prancing Horse’s first production plug-in hybrid spider, the SF90 Spider sets new performance and innovation benchmarks not only for the marque’s range, but for the entire sports car sector.",
    6,
    225000.00,
    875000.00,
    manufacturer_2,
    675,
    210,
    "Car",
)
product_repository.save_product(product_8)

product_9 = Product(
    "AMB 001",
    "The AMB 001 represents the first Brough Superior model to be presented with a turbo-charged engine. The powerful turbo gifts the rider with a motor that has an incredible response and huge torque over a wide range of RPM.",
    2,
    20000.00,
    150000.00,
    manufacturer_4,
    560,
    200,
    "Motorbike",
)
product_repository.save_product(product_9)

product_10 = Product(
    "DB11",
    "DB11 exploits its inner strength and immense performance with completely re-worked chassis, suspension, steering and electronics. Revised suspension with adaptive damping and multiple driver-selectable dynamics enrich DB11’s adaptability.",
    5,
    110000.00,
    430000.00,
    manufacturer_4,
    525,
    192,
    "Car",
)
product_repository.save_product(product_10)
