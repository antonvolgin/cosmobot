#!/bin/python

import logging
from logging import Logger
from datetime import datetime
import app.config as config
import os

log: Logger

def logger_setup(name):
    global log
    log = logging.getLogger(f"{__name__}: {name}")
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    os.makedirs(config.logs_folder, exist_ok=True)
    
    fh = logging.FileHandler("{}{}_{}.log".format(config.logs_folder, name, datetime.now().strftime('%Y%m%d_%H%M%S')))
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    fh.setLevel(logging.DEBUG)
    log.addHandler(fh)

def logger_info(str):
    log.info(str)

def logger_error(str):
    log.error(str)

def logger_exception(str):
    log.exception(str)

def logger_debug(str):
    log.debug(str)
