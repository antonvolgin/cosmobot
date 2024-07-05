#!/bin/python

from decouple import config

database_folder = config('DATABASE_FOLDER')
logs_folder = config('LOGS_FOLDER')
