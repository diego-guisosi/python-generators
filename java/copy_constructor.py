#!/usr/bin/env python3
import sys


def extract_setters(file):

    with open(file, mode="rt") as f:
        setters = [line.strip().split(sep='(')[0].replace("public void ", "")
                   for line in f.readlines() if "public void set" in line]
        return setters


def main(file):

    setters = extract_setters(file)
    for setter in setters:
        getter = setter.replace("set", "get")
        print("this.{set}(other.{get}())".format(set=setter, get=getter))


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print("Provide the file path to the class whose constructor body must be created", file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])


# ~/workspace/sts-3.9.2.RELEASE/classes/src/classes/