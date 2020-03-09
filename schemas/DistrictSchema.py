"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - District schema.
"""

from app import ma

class DistrictSchema(ma.Schema):
    class Meta:
        fields = ('district_code', 'district_name')