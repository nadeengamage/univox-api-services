"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Diploma Schema.
"""

from app import ma
from models.Diploma import Diploma

class DiplomaSchema(ma.ModelSchema):
    class Meta:
        model = Diploma
        fields = ('dip_code', 'dip_name', 'duration', 'status')