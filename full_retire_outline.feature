# James Diller
# 2021FA.CSC.256.0001
# Unit 13 - Retirement Behavioral Test (Unit 13)
# 2021/11/14

#Language Python

Feature : Retirement Age
	As a worker,
	I wish to know
	when I can retire

@automated
Scenario Outline : Inputting various birth dates
	Given Initial input
	When Given <bMonth>
	And <bYear>
	Then we will get a retirement age <rAgeYears> and <rAgeMonths>
	And a retirement date of <rDateMonth> of <rDateYear>

	Examples: Dates
		| bMonth | bYear | rAgeYears | rAgeMonths | rDateMonth | rDateYear |
		| 1	| 1900 | 65 | 0 | 1 | 1965 |
		| 12 | 1937 | 65 | 0 | 12 | 2002 |
		| 1 | 1938 | 65 | 2 | 3 | 2002 |
		| 12 | 1959 | 66 | 10 | 10 | 2026 |
		| 1 | 1960 | 67 | 0 | 1 | 2027 |
		| 12 | 2021 | 67 | 0 | 12 | 2088 |
