import json

import yaml


def parse_file(file):
	with open(file) as f:
		if file.endswith('.json'):
			return json.load(f)
		elif file.endswith(('.yaml', '.yml')):
			return yaml.safe_load(f)
		else:
			raise ValueError(f'Unsupported file format: {file}')