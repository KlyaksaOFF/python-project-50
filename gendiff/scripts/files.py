from gendiff.scripts.ast import build_ast
from gendiff.scripts.formatters.stylish import format_stylish
from gendiff.scripts.parse import parse_file
from gendiff.scripts.formatters.plain import format_plain

def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    ast = build_ast(file1, file2)

    if format_name == 'plain':
        result_lines = format_plain(ast)
        return "\n".join(result_lines)

    return format_stylish(ast)
