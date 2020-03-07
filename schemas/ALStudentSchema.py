"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - AL Student schema.
"""

from app import ma
from models.ALStudent import ALStudent

class ALStudentSchema(ma.Schema):
  class Meta:
    model = ALStudent
    fields = ('stream', 'al_index_no', 'z_score', 'al_ict', 'comm_and_media', 'general_english', 'general_common_test')