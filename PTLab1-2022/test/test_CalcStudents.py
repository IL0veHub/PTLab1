# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcStudents import CalcStudents
import pytest



class TestCalcStudents:

    @pytest.fixture()
    def input_data(self):
        data = [
            {'name': 'Иванов', 'score': {'Физика': 42, 'Химия': 76, 'ОБЖ': 100}}, 
            {'name': 'Петров', 'score': {'Физика': 91, 'Химия': 66, 'ОБЖ': 100}}, 
            {'name': 'Наумов', 'score': {'Физика': 99, 'Химия': 98, 'ОБЖ': 100}}
        ]

        rating_scores: RatingsType = ["Наумов"]

        return data, rating_scores


    def test_calc(self, input_data) -> None:
        students = CalcStudents(input_data[0]).calc()
        assert students == input_data[1]
