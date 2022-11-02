# -*- coding: utf-8 -*-
import argparse
import sys

from CalcStudents import CalcStudents
from DataReaderXML import DataReaderXML


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    students = DataReaderXML().read(path)
    print("Students: ", students)

    calc_student = CalcStudents(students).calc()
    print("Students more four: ", calc_student)


if __name__ == "__main__":
    main()
