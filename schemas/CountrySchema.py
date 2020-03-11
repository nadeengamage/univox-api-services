"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import ma

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('country_code', 'country_iso', 'country_name')