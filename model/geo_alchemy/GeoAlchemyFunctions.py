__author__ = 'Anna'
from geoalchemy2 import Geometry
from geoalchemy2.functions import GenericFunction
from sqlalchemy import Float, String, Boolean


class ST_YMax(GenericFunction):
    name = 'ST_YMax'
    type = Float


class ST_XMax(GenericFunction):
    name = 'ST_XMax'
    type = Float


class ST_YMin(GenericFunction):
    name = 'ST_YMin'
    type = Float


class ST_XMin(GenericFunction):
    name = 'ST_XMin'
    type = Float


class ST_SetSRID(GenericFunction):
    name = 'ST_SetSRID'
    type = Geometry('POLYGON')


class ST_Extent(GenericFunction):
    name = 'ST_Extent'
    type = String


class ST_Covers(GenericFunction):
    name = "ST_Covers"
    type = Boolean
