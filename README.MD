
## Introduction


Python script to generate Ramanujan numbers (numbers that can be expressed as the sum 
of two different cubes in two different ways)

For example, 1729 = 10^3 + 9^3 = 12^3 + 1^3


*  ramanujan_test_v1.py

	* Usage
	
		* nohup python3 ramanujan_test_v1.py

* ramanujan_numbers_list.txt

	* a list of some Ramanujan numbers in the format (2, 16, 9, 15, 4104)
	where 2^3 + 16^3 = 9^3 + 15^3 = 4104

* ramanujan_numbers_list2000.txt

	* a list of Ramanujan numbers upto a,b,c,d <= 2000
	where a^2 + b^2 = c^2 + d^2

* ramanujan_numbers_list2001to4000.txt
	* a list of Ramanujan numbers from a,b,c,d > 2000 upto a,b,c,d <= 4000
	where a^2 + b^2 = c^2 + d^2

* combined_numbers.txt
	* combined list of numbers
	cat ramanujan*.txt > combined_numbers.txt
	(, ), and done removed

* hist_ramanujan_numbers.jpg

	* histogram of Ramanujan numbers

* hist_ramanujan_numbers_log10.eps

        * histogram of Ramanujan numbers
        
        * generated using analysis_2.R

* hist_ramanujan_numbers.eps

	* histogram of Ramanujan numbers

* ALL.txt

	* All Ramanujan numbers


## Usage


```python
python ramanujan_test_v1.py
```

## Contact

	* Soumya Banerjee

	* https://sites.google.com/site/neelsoumya


## Manuscript and citation

     * Forthcoming

     * Preprint

          * https://osf.io/bf3pw

banerjee, soumya. 2021. “Ramanujan Cab Numbers: A Recreational Mathematics Activity.” OSF Preprints. November 19. doi:10.31219/osf.io/bf3pw.
