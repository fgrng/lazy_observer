## Top-level python script, that defines the Flask application instance.
## Imports the 'app' variable that is a member of the 'app' package.
from app import app, db
from app.models import Dimension, Subdimension, Indicator

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Dimension': Dimension, 'Subdimension': Subdimension, 'Indicator': Indicator}
