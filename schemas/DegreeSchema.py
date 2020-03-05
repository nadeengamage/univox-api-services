"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Role schema.
"""

from app import ma
from models.Degree import Degree
from schemas.FacultySchema import FacultySchema

class DegreeSchema(ma.ModelSchema):
    # Relation
    faculty = ma.Nested(FacultySchema)
    
    class Meta:
        model = Degree
        fields = ('faculty', 'degree_code', 'degree_name')
