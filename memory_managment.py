#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List




class Memory:
    def __init__(self):
        self.results_list = []
        self.max_capacity = 10

    def add_result(self, matrix1: List[List[float]], matrix2: List[List[float]], result: List[List[float]], operation: str):
        self.results_list.append(matrix1, matrix2, result, operation)

        if len(self.results_list) > self.max_capacity:
            self.results_list.popleft()

    def get_element(self, index: int):
        if index >= 0 and index < len(self.results_list):
            return self.results_list[index]
        else:
            raise ValueError("Podano zły indeks :)")

    def clear_memory(self):
        self.results_list.clear()


matrix_calculator_memory = Memory()








