#!/usr/bin/env python3
import argparse


def parse_args(args=None):
    p = argparse.ArgumentParser()
    add_arguments(p)
    o = p.parse_args(args)
    o.error = p.error
    return o


def add_arguments(parser):
    sbp = parser.add_subparsers()

    p = sbp.add_parser("doc", help="check all works")
    p.set_defaults(mod=build_doc)


def main(o):
    print(getattr(o, "mod", None))
        


def build_doc(o):
    pass
    

if __name__ == '__main__':
    main(parse_args())
