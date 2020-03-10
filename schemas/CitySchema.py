"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import ma

class CitySchema(ma.Schema):
    class Meta:
        fields = ('city_code', 'city_name', 'postal_code')