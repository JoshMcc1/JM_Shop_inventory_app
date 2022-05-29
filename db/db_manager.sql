PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    country_of_origin VARCHAR,
    operating_status BOOLEAN
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR,
    stock_quantity INTEGER,
    buying_cost REAL,
    selling_cost REAL,
    horse_power INTEGER,
    top_speed INTEGER,
    type VARCHAR,
    manufacturer_id INTEGER NOT NULL,
    FOREIGN KEY (manufacturer_id)
    REFERENCES manufacturers (id)
    ON DELETE CASCADE
);