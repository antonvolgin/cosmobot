#!/bin/python

import sqlite3 as sqlite
# import aiosqlite as sqlite
import os 
from app.logger import logger_info, logger_error
import app.config as config

def _db_create_connection():
    conn = None
    try:
        filename = os.path.join(config.database_folder, "cosmo_catalog.db")
        logger_info(f"Database:{filename}")
        conn = sqlite.connect(filename, timeout=60)
        logger_info(f"SQLite3 version: {sqlite.sqlite_version}")
    except sqlite.Error as e:
        logger_error(e)
    finally:
        if conn:
            pass
            # conn.close()
    return conn

def db_select_products():
    conn = _db_create_connection()
    conn.row_factory = sqlite.Row

    sql = f"""
    SELECT * FROM product p
    LEFT JOIN category c ON c.id = p.category_id
    LEFT JOIN brand b ON b.id = p.brand_id;
    """

    logger_info(f"sql: {sql}")

    cur = conn.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    logger_info(f"rows:{len(rows)}")

    return rows 

def db_select_product(barcode: int):
    conn = _db_create_connection()
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

# def db_insert_video(db_conn, eid, path, path_names, name, origin_size, description, created_at, status):
#     logger_info(f"db_insert_video: {eid}, {path}, {path_names}, {name}, {origin_size}, {created_at}, {status}")
#     sql = """
#         INSERT INTO videos(eid, "path", "path_names", name, "type", origin_size, description, created_at, status) VALUES(?,?,?,?,?,?,?,?,?)
#         ON CONFLICT (eid, "path")
#             DO UPDATE SET
#                 "path" = excluded."path",
#                 "path_names" = excluded."path_names",
#                 name = excluded.name,
#                 "type" = excluded."type",
#                 origin_size = excluded.origin_size,
#                 description = excluded.description,
#                 created_at = excluded.created_at,
#                 status = excluded.status;
#     """
#     # print(f'sql: {sql}')
#     db_conn.execute(sql, (eid, path, path_names, name, "video", origin_size, description, created_at, status))
#     db_conn.commit()

# def db_update_video(db_conn, eid, origin_size, downloaded):
#     sql = f"""
#         UPDATE videos
#         SET origin_size = "{origin_size}", downloaded = "{downloaded}"
#         WHERE eid = {eid}
#     """
#     # print(f'sql: {sql}')
#     db_conn.execute(sql)    
#     db_conn.commit()
