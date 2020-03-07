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
    fields = ('nvq_details', 'al_details', 'application_no', 'identity_no', 'student_type', 'initials', 'surename', 'title', 'gender', 'ethnicity', 'address_1', 'address_2', 'city', 'district', 'telephone', 'mobile', 'email', 'preference_1', 'preference_2', 'preference_3', 'status')