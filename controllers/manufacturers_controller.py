from flask import Flask, redirect, render_template, Blueprint, request
from repositories.product_repository import *
from repositories.manufacturer_repository import *
from models.product import Product

manufacturer_blueprint = Blueprint("manufacturers", __name__)
