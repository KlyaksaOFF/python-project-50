import json


def format_json(ast):
	return json.dumps(ast, indent=2)