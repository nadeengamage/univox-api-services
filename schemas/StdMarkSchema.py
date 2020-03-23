"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Student Marks Schema.
"""

from app import ma
from models import StdMarks
from schemas.DegreeSchema import DegreeSchema
from schemas.StudentSchema import StudentSchema

class StdMarkSchema(ma.Schema):

	# Relation
	degree = ma.Nested(DegreeSchema)
	applicant = ma.Nested(StudentSchema)

	class Meta:
		model = StdMarks
		fields = ('applicant', 'degree.degree_code', 'marks', 'remark', 'status')