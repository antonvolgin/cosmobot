#!/bin/python

import sqlite3 as sqlite

# import aiosqlite as sqlite
import os
from app.logger import logger_info, logger_error
import app.config as config


def db_create_connection():
    conn = None
    try:
        filename = os.path.join(config.database_folder, "cosmo_catalog.db")
        logger_info(f"Database:{filename}")
        conn = sqlite.connect(filename, timeout=60, check_same_thread=False)
        logger_info(f"SQLite3 version: {sqlite.sqlite_version}")
    except sqlite.Error as e:
        logger_error(e)
    finally:
        if conn:
            pass
            # conn.close()
    return conn


def db_select_products(page: int = 1, per_page: int = 20, filter: str = None):
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    if filter:
        sql_count = f"""
        SELECT count(*) FROM product p
        WHERE p.barcode LIKE ? OR p.title LIKE ? OR p.components LIKE ? OR p.description LIKE ?;
        """
        cur = conn.execute(
            sql_count, (f"%{filter}%", f"%{filter}%", f"%{filter}%", f"%{filter}%")
        )
    else:
        sql_count = f"""
        SELECT count(*) FROM product p;
        """
        cur = conn.execute(sql_count)

    total = cur.fetchone()[0]

    offset = (page - 1) * per_page

    if filter:
        sql = f"""
        SELECT * FROM product p
        LEFT JOIN category c ON c.id = p.category_id
        LEFT JOIN brand b ON b.id = p.brand_id
        WHERE p.barcode LIKE ? OR p.title LIKE ? OR p.components LIKE ? OR p.description LIKE ?
        LIMIT ? OFFSET ?;
        """
        cur = conn.execute(
            sql,
            (
                f"%{filter}%",
                f"%{filter}%",
                f"%{filter}%",
                f"%{filter}%",
                per_page,
                offset,
            ),
        )
    else:
        sql = f"""
        SELECT * FROM product p
        LEFT JOIN category c ON c.id = p.category_id
        LEFT JOIN brand b ON b.id = p.brand_id
        LIMIT ? OFFSET ?;
        """
        cur = conn.execute(sql, (per_page, offset))

    logger_info(f"sql: {sql}")

    rows = cur.fetchall()
    cur.close()
    conn.close()

    # logger_info(f"rows:{len(rows)}")

    return rows, total


def db_select_logs(
    page: int = 1,
    per_page: int = 20,
    filter: str = None,
    products: str = "products_all",
    created_at_order: str = "DESC",
):
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql_products = ""
    if products == "products_not_found":
        sql_products = " AND product_id IS NULL"
    elif products == "products_found":
        sql_products = " AND product_id IS NOT NULL"

    sql_order = " ORDER BY l.created_at DESC"
    if created_at_order == "ASC":
        sql_order = " ORDER BY l.created_at ASC"

    if filter:
        sql_count = (
            f"""
        SELECT count(*) FROM log l
        WHERE TRUE
        AND (l.barcode LIKE ? OR l.created_at LIKE ? OR l.product_id LIKE ?)
        """
            + sql_products
            + ";"
        )
        cur = conn.execute(sql_count, (f"%{filter}%", f"%{filter}%", f"%{filter}%"))
    else:
        sql_count = (
            f"""
        SELECT count(*) FROM log l
        WHERE TRUE
        """
            + sql_products
            + ";"
        )
        cur = conn.execute(sql_count)

    logger_info(f"sql_count: {sql_count}")

    total = cur.fetchone()[0]

    offset = (page - 1) * per_page

    if filter:
        sql = (
            f"""
        SELECT * FROM log l
        WHERE TRUE
        AND (l.barcode LIKE ? OR l.created_at LIKE ? OR l.product_id LIKE ?)
        """
            + sql_products
            + sql_order
            + f" LIMIT ? OFFSET ?;"
        )
        cur = conn.execute(
            sql,
            (
                f"%{filter}%",
                f"%{filter}%",
                f"%{filter}%",
                per_page,
                offset,
            ),
        )
    else:
        sql = (
            f"""
        SELECT * FROM log l
        WHERE TRUE
        """
            + sql_products
            + sql_order        
            + f" LIMIT ? OFFSET ?;"
        )
        cur = conn.execute(sql, (per_page, offset))

    logger_info(f"sql: {sql}")

    rows = cur.fetchall()
    cur.close()
    conn.close()

    logger_info(f"rows:{len(rows)}")

    return rows, total


def db_select_brands():
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM brand b;
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    logger_info(f"rows:{len(rows)}")

    return rows


def db_select_categories():
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM category;
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    logger_info(f"rows:{len(rows)}")

    return rows


def db_select_product(barcode: int):
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM product p
    WHERE p.barcode = {barcode};
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    row = cur.fetchone()
    cur.close()
    conn.close()

    return row


def db_insert_log(barcode: int, product_id: int):
    logger_info(f"db_insert_log: barcode: {barcode} product_id: {product_id}")

    conn = db_create_connection()
    conn.row_factory = sqlite.Row
    sql = """
        INSERT INTO log(barcode, product_id) VALUES(?,?)
    """
    conn.execute(sql, (barcode, product_id))
    conn.commit()
    conn.close()


def db_select_categories():
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM category c
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    logger_info(f"rows:{len(rows)}")

    return rows


def db_select_brands():
    conn = db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM brand b
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    logger_info(f"rows:{len(rows)}")

    return rows


def db_insert_product(
    barcode: int,
    title: str,
    url: str,
    components: str,
    description: str,
    brand_id: int,
    category_id: int,
):
    logger_info(f"db_insert_product: barcode: {barcode} title: {title} ...")

    conn = db_create_connection()
    conn.row_factory = sqlite.Row
    sql = """
        INSERT INTO product
            (id, barcode, title, url, components, description, brand_id, category_id)
        VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(barcode)
            DO UPDATE SET
                title = excluded.title,
                url = excluded.url,
                components = excluded.components,
                description = excluded.description,
                brand_id = excluded.brand_id, 
                category_id = excluded.category_id;
    """
    conn.execute(
        sql, (barcode, title, url, components, description, brand_id, category_id)
    )
    conn.commit()
    conn.close()


def db_insert_many_product(products: list):
    logger_info(f"db_insert_many_product...")

    conn = db_create_connection()
    conn.row_factory = sqlite.Row
    sql = """
        INSERT INTO product
            (barcode, title, url, components, description, brand_id, category_id)
        VALUES 
            (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(barcode)
            DO UPDATE SET
                title = excluded.title,
                url = excluded.url,
                components = excluded.components,
                description = excluded.description,
                brand_id = excluded.brand_id, 
                category_id = excluded.category_id;
    """
    conn.executemany(sql, products)
    conn.commit()
    conn.close()


def db_insert_many_brand(brands: list):
    logger_info(f"db_insert_many_brands...")

    conn = db_create_connection()
    conn.row_factory = sqlite.Row
    sql = """
        INSERT INTO brand
            (title, description, url, logo)
        VALUES(?, ?, ?, ?)
        ON CONFLICT(title)
            DO UPDATE SET
                description = excluded.description,
                url = excluded.url,
                logo = excluded.logo;
    """
    conn.executemany(sql, brands)
    conn.commit()
    conn.close()
