from src.controllers.general_endpoints import app
from src.controllers.stage_endpoints import app
from src.controllers.team_endpoints import app
import os

port = os.getenv("PORT") or 5500
app.run(debug=True, port=port, host="0.0.0.0")