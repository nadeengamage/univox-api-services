"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Configurations of the application.
"""

# Bootstrap configurations.
def bootstrap(app, db):
    # Load routes
    from api import routes

    # Database
    from models import __all__
    
    db.create_all()
    db.session.commit()
    pass