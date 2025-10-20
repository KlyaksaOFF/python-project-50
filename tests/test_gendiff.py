from gendiff.scripts.gendiff import generate_diff


def test_gendiff():
	path1 = "tests/test_data/file1.json"
	path2 = "tests/test_data/file2.json"

	expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

	result = generate_diff(path1, path2)
	assert result == expected

