"""Print 'Hello pypa' to stdout.
"""

import argparse
try:
    from hellopypa.hellopypa import hello
except ModuleNotFoundError:
    from hellopypa import hello


def get_args():
    args = argparse.ArgumentParser(
        description=__doc__,
        prog='hellopypa',
    )
    help_upper = 'Uppercase'
    args.add_argument(
        '-u',
        '--upper',
        help=help_upper,
        action='store_true',
    )
    return vars(args.parse_args())


def main():
    args = get_args()
    # print(args)
    print(hello(**args))


if __name__ == "__main__":
    main()
