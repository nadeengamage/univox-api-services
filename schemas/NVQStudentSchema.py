"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - NVQ Student schema.
"""

from app import ma
from models.NVQStudent import NVQStudent

class NVQStudentSchema(ma.Schema):
  class Meta:
    model = NVQStudent
    fields = ('index_no', 'diploma', 'remarks', 'permenent_address')