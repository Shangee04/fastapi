from configparser import ConfigParser
import os
conf_path = os.getcwd()
config = ConfigParser()
config.read(conf_path)


config = ConfigParser()
config.read("application.conf")

