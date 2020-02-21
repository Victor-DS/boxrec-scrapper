import logging
import argparse

log = logging.getLogger(__name__)


def main(args=None):
    parser = argparse.ArgumentParser(prog='boxrec-scrapper',
                                     description='A CLI to scrap data from BoxRec')
    subparsers = parser.add_subparsers(help='Sub-commands')

    from .boxer import add_subcommand_boxer
    add_subcommand_boxer(subparsers)

    args = parser.parse_args(args)

    if hasattr(args, 'func'):
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0
