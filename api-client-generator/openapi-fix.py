import re

with open('openapi.json', 'r') as file:
    content = file.read()
    # in the openapi.json file, when a model was defined with type = array and a generic items = {}
    # the "openapi-format" script removes the "items" property
    # e.g. {"items": {}, "type": "array", "title": "Data"}
    # ==>  {"type": "array", "title": "Data"}
    #
    # this puts the empty "items" property back when it is missing
    # this assumes the "items" field will always immediately follow the "type" one if it is present, and that
    # there will not be any property between them
    content = re.sub('("type": "array")(?!,?\n\s*"items")', r'"type": "array", "items": {}', content)

    # note: this could be updated directly in the dubo-api itself
    content = re.sub('"title": "FastAPI"', r'"title": "Dubo API"', content)

with open('openapi.json', 'w') as file:
    file.write(content)
