""" Unit tests for date.py 
"""
################################################################################
# Author: Erica Soo
# July 2022
################################################################################

import pytest
from date import *
import sys

month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def test_date_to_days1():
    date1 = "1000-01-01"
    num_days = date_to_days(date1, month_lengths)
    assert num_days == 365001 # I manually calculated this value: 1000*365+1

def test_find_days1():
    date1 = "2012-01-10"
    date2 = "2012-01-11"
    diff1 = find_days(date1, date2, month_lengths)
    assert diff1 == 0

def test_find_days2():
    date1 = "2012-01-01"
    date2 = "2012-01-10"
    diff1 = find_days(date1, date2, month_lengths)
    assert diff1 == 8

def test_find_days3():
    date1 = "1801-06-13"
    date2 = "1801-11-11"
    diff1 = find_days(date1, date2, month_lengths)
    assert diff1 == 150

def test_find_days4():
    date1 = "2021-12-01"
    date2 = "2017-12-14"
    diff1 = find_days(date1, date2, month_lengths)
    assert diff1 == 1447


def test_invalid1(capsys):
    date1 = "01-01-2020"
    valid_input(date1, month_lengths)
    captured = capsys.readouterr()
    assert captured.out ==  "The date 01-01-2020 is invalid\n"

def test_invalid2(capsys):
    date1 = "20000-01-01"
    valid_input(date1, month_lengths)
    captured = capsys.readouterr()
    assert captured.out ==  "The date 20000-01-01 is invalid\n"

def test_invalid3(capsys):
    date1 = "2022-02-29"
    valid_input(date1, month_lengths)
    captured = capsys.readouterr()
    assert captured.out ==  "The date 2022-02-29 is invalid\n"

def test_invalid4(capsys):
    date1 = "2020-01-01"
    valid_input(date1, month_lengths)
    captured = capsys.readouterr()
    assert captured.out ==  ""
