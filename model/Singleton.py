__author__ = 'Anna'
from PyQt5.QtCore import *


class Singleton(pyqtWrapperType):

    def __init__(cls, name, bases, dict_singleton):

        super(Singleton, cls).__init__(cls, bases, dict_singleton)
        cls._instance = None

    def __call__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

