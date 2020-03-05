"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Student schema.
"""

from app import ma
from models import Student

class StudentSchema(ma.Schema):
  class Meta:
    model = Student