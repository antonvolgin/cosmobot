-- +goose Up
-- +goose StatementBegin
CREATE TABLE brand (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL DEFAULT '',
    description NOT NULL DEFAULT '',
    url NOT NULL DEFAULT '',
    logo NOT NULL DEFAULT ''
);

-- TEXT CHECK(category IN ('компонент', 'шампунь', 'бальзам', 'стайлинг', 'пилинг')) NOT NULL DEFAULT 'компонент'
CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL DEFAULT '',
    description NOT NULL DEFAULT ''
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    barcode INTEGER UNIQUE,
    title TEXT NOT NULL DEFAULT '',
    url TEXT NOT NULL DEFAULT '',
    components TEXT NOT NULL DEFAULT '',
    brand_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brand (id),
    FOREIGN KEY (category_id) REFERENCES category (id) 
);

CREATE TABLE log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at NOT NULL DEFAULT (datetime('now')),
    barcode INTEGER NOT NULL,
    product_id INTEGER
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE log;
DROP TABLE brand;
DROP TABLE category;
DROP TABLE product;
-- +goose StatementEnd
