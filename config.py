import os

# define the paths to the CNN
model_path = 'assets/models/pokedex.model'

# define the set of class labels (these were derived from the
# 	# label binarizer from the previous post)
labels = ["bulbasaur", "charmander", "mewtwo", "pikachu",
		  "squirtle"]

db_path = os.path.sep.join(["assets", "models", "pokemon_db.json"])

pokedex_img_path = os.path.sep.join(["assets", "images", "pokedex.png"])
default_img_path = os.path.sep.join(["assets", "images", "default.png"])
