"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Faculty schema.
"""

from app import ma
from models import Faculty

class FacultySchema(ma.Schema):
  class Meta:
    fields = ('faculty_code', 'faculty_name')