# James Diller
# 2021FA.CSC.256.0001
# Unit 14 - Retirement Behavioral Test (Unit 14)
# 2021/11/21

#Language Python

Feature: Retirement Age
	As a worker,
	I wish to know
	when I can retire

	Scenario: Set Single Birth Date
		Given A person is born
		When They were born on January 1900
		Then They can expect to retire at 65 years and 0 months, or January 1965

	@automated
	Scenario Outline: Testing Retirement Ages
		Given Initial input
		When Given "<bMonth>" and "<bYear>"
		Then we will get a retirement age "<rAgeYears>" and "<rAgeMonths>"

		Examples: Dates
			| bMonth | bYear | rAgeYears | rAgeMonths |
			| 1	| 1900 | 65 | 0 |
			| 12 | 1937 | 65 | 0 |
			| 1 | 1938 | 65 | 2 |
			| 12 | 1959 | 66 | 10 |
			| 1 | 1960 | 67 | 0 |
			| 12 | 2021 | 67 | 0 |
