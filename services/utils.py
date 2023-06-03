import re

def metadata_str_to_dict(meta_str: str) -> dict:
    dict_meta = {}
    pattern = r'(\w+)[\s]*:[\s]*"([^"]*)"'
    matches = re.findall(pattern, meta_str.strip())

    for match in matches:
        key = match[0]
        value = match[1]

        dict_meta[key] = value

    return dict_meta
