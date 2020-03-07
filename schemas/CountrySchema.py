"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Country schema.
"""

from app import ma

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('country_code', 'country_iso', 'country_name')