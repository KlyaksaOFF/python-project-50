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