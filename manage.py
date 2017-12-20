from asyncio import get_event_loop
from argparse import ArgumentParser
from inspect import iscoroutinefunction

from imaginarium.bin import COMMANDS


loop = get_event_loop()


def get_parser():
    parser = ArgumentParser()
    subparser = parser.add_subparsers()
    for command in COMMANDS:
        parser_command = subparser.add_parser(command.get_name(),
                                              help=command.get_help())
        for args, kwargs in command.get_arguments():
            parser_command.add_argument(*args, **kwargs)

        parser_command.set_defaults(func=command.run)

    return parser


async def run(func, args):
    if iscoroutinefunction(func):
        return await func(loop=loop, **args)

    return func(**args)


if __name__ == '__main__':
    parser = get_parser()
    arguments = parser.parse_args()
    loop.run_until_complete(run(arguments.func, vars(arguments)))
