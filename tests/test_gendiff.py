from gendiff.scripts.gendiff import generate_diff

expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

def test_gendiff():
	json = generate_diff("tests/test_data/file1.json", "tests/test_data/file2.json")
	ymal = generate_diff("tests/test_data/file1.yaml", "tests/test_data/file2.yaml")
	assert json == expected
	assert ymal == expected


def test_mix_format():
	mix = generate_diff("tests/test_data/file1.yaml", "tests/test_data/file2.json")
	assert mix == expected