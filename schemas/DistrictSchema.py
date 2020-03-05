"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - District schema.
"""

from app import ma

class DistrictSchema(ma.Schema):
    class Meta:
        fields = ('district_code', 'district_name')