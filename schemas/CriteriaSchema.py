"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Criteria schema.
"""

from app import ma
from models.Criteria import Criteria
from schemas.DegreeSchema import DegreeSchema

class CriteriaSchema(ma.Schema):

  # Relation
  degree = ma.Nested(DegreeSchema)

  class Meta:
    model = Criteria
    fields = ('degree', 'btch_one_stud_per_program', 'btch_two_stud_per_program', 'first_exam_paper_mark', 'second_exam_paper_mark', 'btch_one_cut_off_mark', 'btch_two_cut_off_mark', 'crt_btch_one_al_cut_off_mark', 'status')
