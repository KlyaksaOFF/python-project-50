def format_plain(ast, path=""):
	lines = []

	for node in ast:
		current_path = f"{path}.{node['key']}" if path else node['key']
		node_type = node['type']

		if node_type == 'nested':
			nested_lines = format_plain(node['children'], current_path)
			lines.extend(nested_lines)
		elif node_type == 'added':
			value = format_value_plain(node['value'])
			lines.append(f"Property '{current_path}' "
			f"was added with value: {value}")
		elif node_type == 'removed':
			lines.append(f"Property '{current_path}' was removed")
		elif node_type == 'changed':
			old_value = format_value_plain(node['old_value'])
			new_value = format_value_plain(node['new_value'])
			lines.append(f"Property '{current_path}' was updated. "
			f"From {old_value} to {new_value}")

	return lines


def format_value_plain(value):
	if isinstance(value, dict):
		return '[complex value]'
	elif isinstance(value, str):
		return f"'{value}'"
	elif value is None:
		return 'null'
	elif isinstance(value, bool):
		return str(value).lower()
	else:
		return value