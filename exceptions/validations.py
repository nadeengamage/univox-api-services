"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Exceptions.
"""

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
