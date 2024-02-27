"""Input for exsextractor"""

# input.py


import argparse


def get_input_from_list_file (data: list|dict, config: dict):
    if isinstance(data, dict):
        list_sheet = None
        if 'list' in data and 'sheets' in data['list'] and 'list_sheet' in data['list']['sheets']:
            list_sheet = data['list']['sheets']['list_sheet']
        if ('list' in data and 'file_name' in data['list']):
            if data['list']['file_name'].endswith('.xlsx'):
                return get_input_from_file_list_xlsx(data['list']['file_name'], list_sheet)
            if data['list']['file_name'].endswith('.csv'):
                return get_input_from_file_list_csv(data['list']['file_name'], config['delimiter'])

    elif data[0].endswith('.xlsx'):
        return get_input_from_file_list_xlsx(data[0], data[1] if len(data) > 1 else None)
    elif data[0].endswith('.csv'):
        return get_input_from_file_list_csv(data[0], config['delimiter'])
    print("File type not supported")
    print(data)
    

def get_input_from_file_list_xlsx (file_name: str, list_sheet: str|None = None):
    input_files = []
    # TODO    
    return input_files


def get_input_from_file_list_csv (file_name: str, delimiter: str = ';'):
    input_files = []
    # TODO    
    return input_files


def get_input_from_args_config (args: argparse.Namespace, config: dict):
    input_files = []
    if (args.check('--input')):
        input_files.extend(args.input)
    if (args.check('--list')):
        input_files.extend(get_input_from_list_file(args.list, config))
    if (args.check('--list-config')):
        input_files.extend(get_input_from_list_file(args.list_config, config))
    if ('input' in config):
        input_files.append(config['input'])
    if ('list' in config and 'file_name' in config['list'] and config['list']['file_name'] != None):
        input_files.extend(get_input_from_list_file(config['list'], config))
    if ('list_config' in config and 'file_name' in config['list_config'] and config['list_config']['file_name'] != None):
        input_files.extend(get_input_from_list_file(config['list_config'], config))
    return input_files