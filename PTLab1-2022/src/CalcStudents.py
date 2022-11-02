# -*- coding: utf-8 -*-
from Types import DataType


class CalcStudents:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating = {}

    def calc(self):
        student_more_four = []
        for student in self.data:
            is_less_four = False
            for key, value in student.get('score').items():
                if value < 76:
                    is_less_four = True
            if not is_less_four:
                student_more_four.append(student.get('name'))
        return student_more_four
