"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Role schema.
"""

from app import ma

class DegreeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'faculty_id', 'degree_code', 'degree_name')
