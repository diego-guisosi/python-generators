#!/usr/bin/env python3
import sys


def extract_setters(file):

    """
    Extract setters from the provided file

    :param file: Path to the class whose setters must be extracted
    :return: iterable containing all setters extracted from the provided file
    """
    with open(file, mode="rt") as f:
        return [line.strip().split(sep='(')[0].replace("public void ", "")
                for line in f.readlines() if "public void set" in line]


def main(file):

    """
    Generate getters based on the setters extracted from file and prints the body of the copy constructor

    :param file: Path to the class whose copy constructor body must me generated
    """
    setters = extract_setters(file)
    for setter in setters:
        getter = setter.replace("set", "get")
        print("this.{set}(other.{get}());".format(set=setter, get=getter))


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print("Provide the file path to the class whose constructor body must be created", file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])
