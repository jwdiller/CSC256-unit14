# James Diller
# 2021FA.CSC.256.0001
# Unit 14 - pytest_bdd
# 2021/11/21
from typing import Dict, Type

import pytest
from pytest_bdd import given, when, then, scenario, scenarios, parsers
from new_retirement_calc import retiree


# scenario

@scenario('full_retire_outline.feature', 'Set Single Birth Date')
def test_after():
    pass


@given('A person is born', target_fixture='worker')
def worker():
    return retiree()


@when('They were born on January 1900')
def worker_born(worker):
    worker.set_birthdate(1900, 1)


@then('They can expect to retire at 65 years and 0 months, or January 1965')
def worker_retire(worker):
    w_age = worker.age()
    assert w_age[0] == 65 and w_age[1] == 0


##################################################################
EXTRA_TYPES = dict(Number=int)

CONVERTER: dict[str, Type[int]] = dict(bMonth=int, bYear=int, rAgeYears=int, rAgeMonths=int)


@scenario("full_retire_outline.feature","Testing Retirement Ages",)
@given('Initial input', target_fixture='work')
def work():
    return retiree()


@when('Given "<bMonth>" and "<bYear>"')
def input_date(work, bMonth, bYear):
    work.set_birthdate(bYear, bMonth)


@then('we will get a retirement age "<rAgeYears>" and "<rAgeMonths>"')
def correct_age(work, rAgeYears, rAgeMonths):
    check_age = work.age()
    assert rAgeYears == check_age[0] and rAgeMonths == check_age[1]
