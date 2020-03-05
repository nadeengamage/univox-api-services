"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - City schema.
"""

from app import ma

class CitySchema(ma.Schema):
    class Meta:
        fields = ('city_code', 'city_name', 'postal_code')