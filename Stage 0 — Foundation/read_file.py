import json

def get_recipes(file_name):
   with open(file_name, "r") as f:
      #content = f.read().strip()
      dict = json.load(f)

   return dict