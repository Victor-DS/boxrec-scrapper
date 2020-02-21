from boxrec.parser.boxer_parser import get_data as boxer_parser


def add_subcommand_boxer(subparsers):
    parser = subparsers.add_parser('boxer', help='Scrap a boxer\'s data')
    parser.add_argument('--id', '-i', type=int, dest='id', required=True,
                        help='The Boxer\'s ID on BoxRec')
    parser.add_argument('--output', '-o', type=str, dest='filename', default='output',
                        help='The filename name to save the JSON results (without extension)')
    parser.set_defaults(func=boxer)


def boxer(args):
    boxer_data = boxer_parser(args.id)
    with open(args.filename + '.json', 'w') as file:
        file.write(boxer_data)
