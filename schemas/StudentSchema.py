"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Student schema.
"""

from app import ma
from models import Student
from schemas.NVQStudentSchema import NVQStudentSchema
from schemas.ALStudentSchema import ALStudentSchema

class StudentSchema(ma.Schema):

  # Relation
  nvq_details = ma.Nested(NVQStudentSchema)
  al_details = ma.Nested(ALStudentSchema)

  class Meta:
    model = Student
    fields = ('nvq_details', 'al_details', 'identity_no', 'student_type', 'marital_status', 'initials', 'surename', 'title', 'gender', 'ethnicity', 'address_1', 'address_2', 'address_3', 'city', 'district', 'permanent_district','telephone', 'mobile', 'email', 'preference_1', 'preference_2', 'preference_3', 'status')