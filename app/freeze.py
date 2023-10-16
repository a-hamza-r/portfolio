"""Build the site."""

import os
import yaml

from flask_frozen import Freezer
from run import app

with open(".config.yml", "r") as config_file:
    config_data = yaml.safe_load(config_file)

# add the path where you want your static files to be generated
OUTPUT_DIR = config_data["path_to_static_website"]

app.debug = False
app.config["FREEZER_DESTINATION"] = OUTPUT_DIR
freezer = Freezer(app)


if __name__ == "__main__":
    freezer.freeze()
    print("Written to: " + OUTPUT_DIR)
