# -*- coding: utf-8 -*-
# -- ---------------------------------------------------------------------------
# --
# -- Title:        run.py
# -- License:      Apache License Version 2.0
# -- Author:       Ethan Dunford
# -- Version:      1
# -- Date:         17/03/17
# --
# -- ---------------------------------------------------------------------------
import sqlite3
import os


class SqlLite(object):

    def __init__(self, database_name):
        self.database_name = database_name
        self.file_path     = os.path.dirname(os.path.abspath(__file__)) + '/'
        if not os.path.exists(self.file_path + self.database_name):
            print 'No database found creating database'
            conn = sqlite3.connect(self.database_name)

        else:
            print ' Database found'

    def run_db(self, sql, params={}):
        data = None
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                data   = cursor.fetchall()
                if data is not None and len(data) > 0:
                    return data
        except Exception as e:
            print str(e)

    def exe_db(self, sql, params={}):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                conn.commit()
        except Exception as e:
            print str(e)

    def bulk_insert(self):
        return

    def export_to_sql(self, file_name):
        with sqlite3.connect(self.database_name) as conn:
            with open(file_name, 'w') as f:
                for line in conn.iterdump():
                    f.write('%s\n' % line)
