"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - NVQ Student schema.
"""

from app import ma
from models import NVQStudent

class NVQStudentSchema(ma.Schema):
  class Meta:
    model = NVQStudent