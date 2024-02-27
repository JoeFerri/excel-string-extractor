"""Excel String Extractor"""

# exsextractor.py


import os

from .args import parse_args
from .config import ConfigType
from .config import get_config_by_template
from .config import config_align
from .config import config_2align
from .config import check_config_list_config
from .config import get_config_from_sheet
from .config import get_config_from_file
from .input import get_input_from_args_config


CONF_TEMPLATE_JSON_PATH = os.path.join('exsextractor', 'template', 'conf.template.json')


def main ():
    (parser, args) = parse_args()
    # print(args)


    # configurazione
    config = get_config_by_template(CONF_TEMPLATE_JSON_PATH)

    config_align(config, args)

    if (args.check('--config')):
        config_2 = get_config_from_file(args.config[0])
        if (args.check('--input') or args.check('--list') or args.check('--list-config')):
            if (args.check('list-config')):
                parser.print_exit('''argument -co/--config: not allowed with argument -lc/--list-config''')
            try:
                check_config_list_config(config_2)
            except Exception as e:
                parser.print_exit(e)
            config_2align(config, config_2, ConfigType.INPUT if args.check('input') else ConfigType.LIST)
        else:
            # è stato passato soltanto un file di configurazione
            if ('input' in config_2 and 'list' in config_2 and 'file_name' in config_2):
                parser.print_exit('''config must contain either "input", or "list"''')
            config_2align(config, config_2, ConfigType.CONFIG)

    if (args.check('--list-config')):
        # assumo che non sia stato passato un file di configurazione separato e che
        # non siano stati passati --input e --list
        config_2 = get_config_from_sheet(args.list_config)
        try:
            check_config_list_config(config_2)
        except Exception as e:
            parser.print_exit(e)
        config_2align(config, config_2, ConfigType.LIST_CONFIG)
    
    
    # lista dei file di input
    input_files = get_input_from_args_config(args, config)

    print("\n", config)
    print("\n", input_files)