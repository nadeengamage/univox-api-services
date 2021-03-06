"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Load all sub modules in the project.
"""

# Auth
from api.auth import auth

# Role
from api.user import roles 

# User
from api.user import users 

# Country
from api.country import countries

# District
from api.district import districts

# City
from api.city import cities

# Faculty
from api.faculty import faculties

# Degree
from api.degree import degrees

# Criteria
from api.degree import criterias

# Applicant
from api.student import applicants

# Applicant Marks
from api.student import marks

# Diploma
from api.diploma import diplomas

#Report
from api.report import reports