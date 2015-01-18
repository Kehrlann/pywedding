#coding=utf-8

import config

from flask import Flask
import config

app = Flask(__name__)

# Chargement de la config par défaut
app.config.from_object(config)

# Overload default cfg with the one in the envvar
try:
    app.config.from_envvar('PYWEDDING_CONFIG')
    print "Loaded external config"
except RuntimeError as rte:
    print "error loading the external config, it should be specified in env_var : PYWEDDING_CONFIG"
except IOError as ioe:
    print "the confing file specified in PYWEDDING_CONFIG doesn't exist"
#
#
# import os.path
#
# db_path = app.config['DB_PATH']
# if db_path is None :
#     db_path = os.path.join(os.path.expanduser("~"), "wedding.sqlite")
#     print "No filename argument specified. Your database will be in %s" % db_path
#
# from init_db import init_db
#
# init_db(db_path)
#
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite+pysqlite:///%s' % db_path)
# DBSession = sessionmaker(bind=engine)


app.jinja_env.globals['site_name']          =   app.config['SITE_NAME']
app.jinja_env.globals['info']               =   app.config['INFO_LINK']
app.jinja_env.globals['wishlist']           =   app.config['WISHLIST_LINK']
app.jinja_env.globals['accommodation']      =   app.config['ACCOMMODATION_LINK']
app.jinja_env.globals['honeymoon']          =   app.config['HONEYMOON_LINK']

import views
