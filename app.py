"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Bootloader of the application.
"""

import os
from api import create_app
from core import bootstrap
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

# Initialize the application
app = create_app()

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Load configuration
bootstrap()


# Main configurations
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG'))
    pass