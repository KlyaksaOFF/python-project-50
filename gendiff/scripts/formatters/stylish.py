from gendiff.scripts.format_value import format_value


def format_stylish(ast, depth=0):
    indent = "  " * depth
    lines = []

    for node in ast:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            nested = format_stylish(node['children'], depth + 2)
            lines.append(f"{indent}    {key}: {nested}")
        elif node_type == 'added':
            value = format_node_value(node['value'],
			depth, is_added_removed=True)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == 'removed':
            value = format_node_value(node['value'],
			depth, is_added_removed=True)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == 'changed':
            old_val = format_node_value(node['old_value'], depth)
            new_val = format_node_value(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old_val}")
            lines.append(f"{indent}  + {key}: {new_val}")
        else:
            value = format_node_value(node['value'], depth)
            lines.append(f"{indent}    {key}: {value}")

    result = "{\n" + "\n".join(lines) + "\n" + indent + "}"
    return result


def format_node_value(value, depth, is_added_removed=False):
    if isinstance(value, dict):
        return build_unchanged(value, depth + 2)
    else:
        return format_value(value)


def build_unchanged(data, depth):
    indent = "  " * depth
    lines = []

    for key, value in sorted(data.items()):
        if isinstance(value, dict):
            nested = build_unchanged(value, depth + 2)
            lines.append(f"{indent}    {key}: {nested}")
        else:
            lines.append(f"{indent}    {key}: {format_value(value)}")

    return "{\n" + "\n".join(lines) + "\n" + indent + "}"