from flask import Flask, redirect, render_template, Blueprint, request
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
from models.product import Product

product_blueprint = Blueprint("products", __name__)


@product_blueprint.route("/products")
def get_products():
    filter = None
    manufacturers = manufacturer_repository.select_all_manufacturers()
    products = product_repository.select_all_products()
    active_products = []
    product_types = []
    for product in products:
        if product.manufacturer.operating_status == True:
            active_products.append(product)
        if not product_types.__contains__(product.type):
            product_types.append(product.type)

    return render_template(
        "/products/index.html",
        products=active_products,
        filter=filter,
        manufacturers=manufacturers,
        product_types=product_types,
    )


@product_blueprint.route("/products/type", methods=["POST"])
def get_products_by_type():
    filter = request.form["type"]
    manufacturers = manufacturer_repository.select_all_manufacturers()
    products = product_repository.select_all_products()
    product_types = []
    active_products = []
    for product in products:
        if product.manufacturer.operating_status == True:
            active_products.append(product)
        if not product_types.__contains__(product.type):
            product_types.append(product.type)

    return render_template(
        "/products/index.html",
        products=active_products,
        filter=filter,
        manufacturers=manufacturers,
        product_types=product_types,
    )


@product_blueprint.route("/products/manufacturer", methods=["POST"])
def get_products_by_manufacturer():
    filter = request.form["manufacturer"]
    manufacturers = manufacturer_repository.select_all_manufacturers()
    products = product_repository.select_all_products()
    product_types = []
    active_products = []
    for product in products:
        if product.manufacturer.operating_status == True:
            active_products.append(product)
        if not product_types.__contains__(product.type):
            product_types.append(product.type)

    return render_template(
        "/products/index.html",
        products=active_products,
        filter=filter,
        manufacturers=manufacturers,
        product_types=product_types,
    )


@product_blueprint.route("/products/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select_product(id)
    mark_up = product.calculate_markup()
    return render_template("products/show.html", product=product, mark_up=mark_up)


@product_blueprint.route("/products/new")
def add_product():
    manufacturers = manufacturer_repository.select_all_manufacturers()
    active_manufacturers = []
    for manufacturer in manufacturers:
        if manufacturer.operating_status == True:
            active_manufacturers.append(manufacturer)
    return render_template("/products/new.html", manufacturers=active_manufacturers)


@product_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_cost = request.form["selling_cost"]
    manufacturer_id = request.form["manufacturer_id"]
    horse_power = request.form["horse_power"]
    top_speed = request.form["top_speed"]
    type = request.form["type"]
    manufacturer = manufacturer_repository.select_manufacturer(manufacturer_id)
    product = Product(
        name,
        description,
        stock_quantity,
        buying_cost,
        selling_cost,
        manufacturer,
        horse_power,
        top_speed,
        type,
    )
    product_repository.save_product(product)
    return redirect("/products")


@product_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select_product(id)
    manufacturers = manufacturer_repository.select_all_manufacturers()
    active_manufacturers = []
    for manufacturer in manufacturers:
        if manufacturer.operating_status == True:
            active_manufacturers.append(manufacturer)
    return render_template(
        "/products/edit.html", product=product, manufacturers=manufacturers
    )


@product_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_cost = request.form["selling_cost"]
    manufacturer_id = request.form["manufacturer_id"]
    horse_power = request.form["horse_power"]
    top_speed = request.form["top_speed"]
    type = request.form["type"]
    manufacturer = manufacturer_repository.select_manufacturer(manufacturer_id)
    product = Product(
        name,
        description,
        stock_quantity,
        buying_cost,
        selling_cost,
        manufacturer,
        horse_power,
        top_speed,
        type,
        id,
    )
    product_repository.update_product(product)
    return redirect("/products")


@product_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete_product(id)
    return redirect("/products")
