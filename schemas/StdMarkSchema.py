"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Student Marks Schema.
"""

from app import ma
from models import StdMarks

class StdMarkSchema(ma.Schema):
  class Meta:
    model = StdMarks
    fields = ('student_id', 'degree_id', 'marks', 'remark', 'status')