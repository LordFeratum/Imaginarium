from argparse import ArgumentParser

from imaginarium.bin import COMMANDS


def get_parser():
    parser = ArgumentParser()
    subparser = parser.add_subparsers()
    for command in COMMANDS:
        parser_command = subparser.add_parser(command.get_name(),
                                              help=command.get_help())
        for argument in command.get_arguments():
            parser_command.add_argument(
                argument['name'], argument['small_name'],
                type=argument['type'], required=argument['required']
            )

        parser_command.set_defaults(func=command.run)

    return parser


if __name__ == '__main__':
    parser = get_parser()
    arguments = parser.parse_args()
    arguments.func(**vars(arguments))
