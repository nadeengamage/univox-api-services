"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Bootloader of the application.
"""
from api import create_app
from core import bootstrap

# Initialize the application
app = create_app()

# Load configuration
bootstrap()


# Main configurations
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    pass