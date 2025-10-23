import json

from gendiff.scripts.gendiff import generate_diff

expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

expected_children = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_gendiff():

	json = generate_diff("tests/test_data/file1.json",
	"tests/test_data/file2.json")

	ymal = generate_diff("tests/test_data/file1.yaml",
	"tests/test_data/file2.yaml")

	assert json == expected_children
	assert ymal == expected


def test_empty_files():
	result = generate_diff(
		"tests/test_data/empty1.json",
		"tests/test_data/empty2.json"
	)
	assert result == "{\n\n}"


def test_plain_format():
	result = generate_diff(
		"tests/test_data/file1.json",
		"tests/test_data/file2.json",
		'plain'
	)
	expected1 = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

	assert result == expected1


def test_json_format():
	result = generate_diff(
		"tests/test_data/file1.json",
		"tests/test_data/file2.json",
		'json'
	)

	parsed = json.loads(result)
	assert isinstance(parsed, list)

	first_node = parsed[0]
	assert 'key' in first_node
	assert 'type' in first_node
	assert first_node['key'] == 'common'
	assert first_node['type'] == 'nested'
	assert 'children' in first_node