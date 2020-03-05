"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - AL Student schema.
"""

from app import ma
from models import ALStudent

class ALStudentSchema(ma.Schema):
  class Meta:
    model = ALStudent