"""Print 'Hello pypa' to stdout.
"""

from hellopypa import hello
# from hellopypa.hellopypa import hello
import argparse


def get_args():
    args = argparse.ArgumentParser(
        description=__doc__,
        prog='hellopypa',
    )
    help_case = 'casing (c: capitalize; l: lowercase; u: uppercase)'
    args.add_argument(
        '-c',
        '--case',
        help=help_case,
        choices=['c', 'l', 'u']
    )
    return vars(args.parse_args())


def main():
    args = get_args()
    print(hello(**args))


if __name__ == "__main__":
    main()
