"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Criteria schema.
"""

from app import ma
from models import Criteria

class CriteriaSchema(ma.Schema):
  class Meta:
    model = Criteria