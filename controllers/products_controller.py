from flask import Flask, redirect, render_template, Blueprint, request
from repositories.product_repository import *
from repositories.manufacturer_repository import *
from models.product import Product

product_blueprint = Blueprint("products", __name__)
