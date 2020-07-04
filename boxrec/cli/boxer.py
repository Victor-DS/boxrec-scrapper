from boxrec.parser.boxer_parser import get_data as boxer_parser
from boxrec.helper.logger import Logger
import json
import time


class Boxer:

    def __init__(self, log_level):
        self.log = Logger.get_logger(log_level)

    def scrap_boxer(self, args):
        boxer_data = self._get_scrapping_data(args.id, args.sleep)
        self._save_to_file(boxer_data, args.filename)

    def _get_scrapping_data(self, boxer_id_list, sleep):
        boxer_data = {}
        for boxer_id in boxer_id_list:
            self.log.info('Scrapping data for ID: ' + str(boxer_id))
            time.sleep(sleep)
            try:
                boxer_data[boxer_id] = boxer_parser(boxer_id)
            except Exception:
                self.log.error('Failed to scrap boxer with ID: ' + str(boxer_id))
        return boxer_data

    def _save_to_file(self, data, filename):
        data_string = json.dumps(data)
        with open(filename + '.json', 'w') as file:
            file.write(data_string)


def add_subcommand_boxer(subparsers):
    parser = subparsers.add_parser('boxer', help='Scrap a boxer\'s data')
    parser.add_argument('--id', '-i', type=int, dest='id', required=True,  action='append',
                        help='The Boxer\'s ID on BoxRec')
    parser.add_argument('--output', '-o', type=str, dest='filename', default='output',
                        help='The filename name to save the JSON results (without extension)')
    parser.add_argument('--sleep', '-z', type=int, dest='sleep', default=0,
                        help='Time in seconds to wait before scrapping another boxer (used to avoid connection limits)')
    parser.set_defaults(func=execute)


def execute(args):
    boxer = Boxer(args.loglevel.upper())
    boxer.scrap_boxer(args)
