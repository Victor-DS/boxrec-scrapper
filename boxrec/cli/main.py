import argparse
from boxrec.cli.boxer import add_subcommand_boxer


def main(args=None):
    parser = argparse.ArgumentParser(prog='boxrec-scrapper',
                                     description='A CLI to scrap data from BoxRec')
    subparsers = parser.add_subparsers(help='Sub-commands')

    parser.add_argument(
        '--loglevel', default='info', help='Log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
    )

    add_subcommand_boxer(subparsers)

    args = parser.parse_args(args)

    if hasattr(args, 'func'):
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0
