## Tests:
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=KlyaksaOFF_python-project-50)](https://sonarcloud.io/summary/new_code?id=KlyaksaOFF_python-project-50)
[![Actions Status](https://github.com/KlyaksaOFF/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/KlyaksaOFF/python-project-50/actions)
[![Python CI](https://github.com/KlyaksaOFF/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/KlyaksaOFF/python-project-50/actions/workflows/ci.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=KlyaksaOFF_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=KlyaksaOFF_python-project-50)

### Usage:

```bash
# Stylish format (default)
gendiff file1.json file2.json

# Plain format  
gendiff --format plain file1.json file2.json

# JSON format
gendiff --format json file1.json file2.json
```
---
Demo:
https://asciinema.org/a/iend1ttaNKfSgM6R9YO6MmcaV.svg

Development:
Linter: ruff (run with make lint)

Package manager: uv

Tests: pytest