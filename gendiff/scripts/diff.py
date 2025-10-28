def build_diff(data1, data2):
	ast = []
	all_keys = sorted(set(data1.keys()) | set(data2.keys()))

	for key in all_keys:
		value1 = data1.get(key)
		value2 = data2.get(key)

		if key not in data2:
			ast.append({'key': key, 'type': 'removed', 'value': value1})

		elif key not in data1:
			ast.append({'key': key, 'type': 'added', 'value': value2})

		elif isinstance(value1, dict) and isinstance(value2, dict):
			children = build_diff(value1, value2)
			ast.append({'key': key, 'type': 'nested', 'children': children})

		elif value1 != value2:
			ast.append({
				'key': key,
				'type': 'changed',
				'old_value': value1,
				'new_value': value2
			})
		else:
			ast.append({'key': key, 'type': 'unchanged', 'value': value1})

	return ast