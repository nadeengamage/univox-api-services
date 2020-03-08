"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Role schema.
"""

from app import ma

class RoleSchema(ma.Schema):
  class Meta:
    fields = ('role_code', 'role_name')