readme

Python script to generate Ramanujan numbers (numbers that can be expressed as the sum 
of two different cubes in two different ways)
For example, 1729 = 10^3 + 9^3 = 12^3 + 1^3

1) ramanujan_test_v1.py
	Usage - nohup python ramanujan_test_v1.py

2) ramanujan_numbers_list.txt
	a list of some Ramanujan numbers in the format (2, 16, 9, 15, 4104)
	where 2^3 + 16^3 = 9^3 + 15^3 = 4104

3) ramanujan_numbers_list2000.txt
	a list of Ramanujan numbers upto a,b,c,d <= 2000
	where a^2 + b^2 = c^2 + d^2

4) ramanujan_numbers_list2001to4000.txt
	a list of Ramanujan numbers from a,b,c,d > 2000 upto a,b,c,d <= 4000
	where a^2 + b^2 = c^2 + d^2

5) combined_numbers.txt
	combined list of numbers
	cat ramanujan*.txt > combined_numbers.txt
	(, ), and done removed

6) hist_ramanujan_numbers.jpg
	histogram of Ramanujan numbers
