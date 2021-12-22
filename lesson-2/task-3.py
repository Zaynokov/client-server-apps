import yaml

data = {
    'first': ['one', 'two', 'three'],
    'second': 373,
    'third': {
        '1': '100€',
        '2': '200€',
        '3': '300€'
    }
}


def write_dict_to_yaml(dict):
    with open('file.yaml', 'w') as yaml_file:
        yaml.dump(dict, yaml_file, default_flow_style=False, allow_unicode=True)


write_dict_to_yaml(data)