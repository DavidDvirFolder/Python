import os
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_baseURL():
        baseURL = config.get('common info', 'baseURL')
        return baseURL

    @staticmethod
    def get_loginURL():
        loginURL = config.get('common info', 'loginURL')
        print("Current working directory:", os.getcwd())
        print("Config file path:", os.path.abspath(".\\Configurations\\config.ini"))
        return loginURL

    @staticmethod
    def get_email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
