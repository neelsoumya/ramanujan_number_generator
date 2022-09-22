
## Introduction


Python script to generate Ramanujan numbers (numbers that can be expressed as the sum 
of two different cubes in two different ways)

For example, 1729 = 10^3 + 9^3 = 12^3 + 1^3

where ^ denotes exponentiation.

## Installation

Install R

https://www.r-project.org/

R Studio

https://www.rstudio.com/products/rstudio/download/preview/

and Python

https://www.python.org/downloads/

In R run the following commands

```r
install.packages('sqldf')
install.packages('ggplot2')
```

or

```r
install.packages('devtools')
library(devtools)
devtools::install_github('neelsoumya/ramanujan_number_generator')
```

Clone or download the repository

```r
git clone https://github.com/neelsoumya/ramanujan_number_generator
```


## Usage


```python
python ramanujan_test_v1.py
```

```r

R --no-save < analysis.R

```


## Files

*  `ramanujan_test_v1.py`

	* Usage
	
	
		nohup python3 ramanujan_test_v1.py
		
        

* `ramanujan_numbers_list.txt`

	* a list of some Ramanujan numbers in the format (2, 16, 9, 15, 4104)
	where 2^3 + 16^3 = 9^3 + 15^3 = 4104

* `ramanujan_numbers_list2000.txt`

	* a list of Ramanujan numbers upto a,b,c,d <= 2000
	where a^2 + b^2 = c^2 + d^2

* `ramanujan_numbers_list2001to4000.txt`
	* a list of Ramanujan numbers from a,b,c,d > 2000 upto a,b,c,d <= 4000
	where a^2 + b^2 = c^2 + d^2

* `combined_numbers.txt`
	* combined list of numbers
	cat ramanujan*.txt > combined_numbers.txt
	(, ), and done removed

* `hist_ramanujan_numbers.jpg`

	* histogram of Ramanujan numbers

* `hist_ramanujan_numbers_log10.eps`

        * histogram of Ramanujan numbers
        
        * generated using analysis.R

* `hist_ramanujan_numbers.eps`

	* histogram of Ramanujan numbers

* `ALL.txt`

	* All Ramanujan numbers



## Contact

Soumya Banerjee

https://sites.google.com/site/neelsoumya

sb2333@cam.ac.uk

## Other ideas and resources

https://stackoverflow.com/questions/69669784/ramanujans-number-in-c#

https://stackoverflow.com/questions/32876131/making-hardy-ramanujan-nth-number-finder-more-efficient

http://recmath.org/Magic%20Squares/narciss.htm

https://ia801004.us.archive.org/17/items/martingardnerthecolossalbookofmathematics/Martin%20Gardner%20-%20The%20Colossal%20Book%20Of%20Mathematics.pdf

http://jnsilva.ludicum.org/HMR13_14/536.pdf

https://mathoverflow.net/questions/152580/recreational-mathematics-where-to-search

http://www.science.smith.edu/~jhenle/pleasingmath/

## Manuscript and citation

Soumya Banerjee, "Ramanujan Cab Numbers: A Recreational Mathematics Activity," Journal of Humanistic Mathematics, Volume 12 Issue 2 (July 2022), pages 503-517. 

Available at: 

https://scholarship.claremont.edu/jhm/vol12/iss2/29

Preprint

https://osf.io/a2jc9/


banerjee, soumya. 2022. “Ramanujan Cab Numbers: A Recreational Mathematics Activity.” OSF Preprints. May 10. doi:10.31219/osf.io/a2jc9

