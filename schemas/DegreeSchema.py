"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Role schema.
"""

from app import ma

class DegreeSchema(ma.schema):
    class Meta:
        fields = ('id', 'degree_code', 'degree_name')
