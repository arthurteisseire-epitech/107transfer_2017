import argparse
import sys

class add_to_list(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if 'arg' not in namespace:
            namespace.arg = []
        namespace.arg.append((self.dest, values))

def parse_all():
    len_args = len(sys.argv) - 1
    tab = []
    parser = argparse.ArgumentParser()
    for i in range(0, len_args // 2):
        parser.add_argument("num", type=str, help="polynomial numerator defined by its coeficients", action=add_to_list)
        parser.add_argument("den", type=str, help="polynomial denominator defined by its coeficients", action=add_to_list)
    args = parser.parse_args()
    for i in args.arg:
        tab.append(list(map(int, i[1].split('*'))))
    return (tab)
