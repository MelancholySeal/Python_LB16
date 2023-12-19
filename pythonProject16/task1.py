#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module1

if __name__ == "__main__":
    cnt = module1.outer_function()

    k = float(input("Введите значение k: "))

    result = cnt(k)

    print(f"Результат: {result}")
