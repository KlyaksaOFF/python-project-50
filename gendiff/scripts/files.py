import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)

    lines = []
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    for key in all_keys:
        if key not in file2:
            lines.append(f"  - {key}: {file1[key]}")
        elif key not in file1:
            lines.append(f"  + {key}: {file2[key]}")
        elif file1[key] != file2[key]:
            lines.append(f"  - {key}: {file1[key]}")
            lines.append(f"  + {key}: {file2[key]}")
        else:
            lines.append(f"    {key}: {file1[key]}")
    result = "{\n" + "\n".join(lines) + "\n}"
    return result

