from db.run_sql import run_sql

from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository


def select_all_products():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select_manufacturer(
            row["manufacturer_id"]
        )
        product = Product(
            row["name"],
            row["description"],
            row["stock_quantity"],
            row["buying_cost"],
            row["selling_cost"],
            manufacturer,
            row["horse_power"],
            row["top_speed"],
            row["type"],
            row["id"],
        )
        products.append(product)

    return products


def select_product(id):
    product = None
    sql = "SELECT * FROM products WHERE id=?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select_manufacturer(
            result["manufacturer_id"]
        )
        product = Product(
            result["name"],
            result["description"],
            result["stock_quantity"],
            result["buying_cost"],
            result["selling_cost"],
            manufacturer,
            result["horse_power"],
            result["top_speed"],
            result["type"],
            result["id"],
        )

    return product


def save_product(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id, horse_power, top_speed, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING *"
    values = [
        product.name,
        product.description,
        product.stock_quantity,
        product.buying_cost,
        product.selling_cost,
        product.manufacturer.id,
        product.horse_power,
        product.top_speed,
        product.type,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    product.id = id
    return product


def delete_all_products():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete_product(id):
    sql = "DELETE FROM products WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update_product(product):
    sql = "UPDATE products set (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id, horse_power, top_speed, type) = (?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [
        product.name,
        product.description,
        product.stock_quantity,
        product.buying_cost,
        product.selling_cost,
        product.manufacturer.id,
        product.horse_power,
        product.top_speed,
        product.type,
        product.id,
    ]
    run_sql(sql, values)
