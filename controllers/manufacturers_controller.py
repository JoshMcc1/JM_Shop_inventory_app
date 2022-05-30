from flask import Flask, redirect, render_template, Blueprint, request
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
from models.manufacturer import Manufacturer

manufacturer_blueprint = Blueprint("manufacturers", __name__)


@manufacturer_blueprint.route("/manufacturers")
def get_manufacturers():
    manufacturers = manufacturer_repository.select_all_manufacturers()
    return render_template("/manufacturers/index.html", manufacturers=manufacturers)


@manufacturer_blueprint.route("/manufacturers/<id>", methods=["GET"])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select_manufacturer(id)
    return render_template("/manufacturers/show.html", manufacturer=manufacturer)


@manufacturer_blueprint.route("/manufacturers/new")
def add_manufacturer():
    return render_template("/manufacturers/new.html")


@manufacturer_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    country_of_origin = request.form["country_of_origin"]
    operating_status = bool(int(request.form["operating_status"]))
    manufacturer = Manufacturer(name, country_of_origin, operating_status)
    manufacturer_repository.save_manufacturer(manufacturer)
    return redirect("/manufacturers")


@manufacturer_blueprint.route("/manufacturers/<id>/edit", methods=["GET"])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select_manufacturer(id)
    return render_template("/manufacturers/edit.html", manufacturer=manufacturer)


@manufacturer_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    country_of_origin = request.form["country_of_origin"]
    operating_status = bool(int(request.form["operating_status"]))
    manufacturer = Manufacturer(name, country_of_origin, operating_status, id)
    manufacturer_repository.update_manufacturer(manufacturer)
    return redirect("/manufacturers")


@manufacturer_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete_manufacturer(id)
    return redirect("/manufacturers")
