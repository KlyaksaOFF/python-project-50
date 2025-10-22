from gendiff.scripts.ast import build_ast
from gendiff.scripts.formatters.stylish import format_stylish
from gendiff.scripts.parse import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
	file1 = parse_file(file_path1)
	file2 = parse_file(file_path2)
	ast = build_ast(file1, file2)

	if format_name == 'stylish':
		return format_stylish(ast)

	return format_stylish(ast)
