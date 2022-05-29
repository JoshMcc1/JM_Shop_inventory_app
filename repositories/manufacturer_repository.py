from db.run_sql import run_sql

from models.manufacturer import Manufacturer


def select_all_manufacturers():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        operating_status = True if row["operating_status"] == 1 else False
        manufacturer = Manufacturer(
            row["name"], row["country_of_origin"], operating_status, row["id"]
        )
        manufacturers.append(manufacturer)

    return manufacturers


def select_manufacturer(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        operating_status = True if result["operating_status"] == 1 else False
        manufacturer = Manufacturer(
            result["name"], result["country_of_origin"], operating_status, result["id"]
        )

    return manufacturer


def save_manufacturer(manufacturer):
    sql = "INSERT INTO manufacturers (name, country_of_origin, operating_status) VALUES (?, ?, ?) RETURNING *"
    values = [
        manufacturer.name,
        manufacturer.country_of_origin,
        manufacturer.operating_status,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    manufacturer.id = id
    return manufacturer


def delete_all_manufacturers():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)


def delete_manufacturer(id):
    sql = "DELETE FROM manufacturers WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update_manufacturer(manufacturer):
    sql = "UPDATE manufacturers SET (name, country_of_origin, operating_status) = (?, ?, ?) WHERE id = ?"
    values = [
        manufacturer.name,
        manufacturer.country_of_origin,
        manufacturer.operating_status,
        manufacturer.id,
    ]
    run_sql(sql, values)
