#####################################################################################
# Generic function to analyze distribution of Ramanujan numnbrs
#
# Usage: nohup R --no-save < analysis.R
# OR
# R # then
# source("analysis_2.R")
#
# Installation:
# install.packages('sqldf')
#
####################################################################################

######################################
# Load required packages
######################################
library(sqldf)
library(ggplot2)

######################################
# Read in file of akk numbers
######################################

# NOTE: file created using
# cat ramanujan*.txt > combined_numbers.txt
# (, ), and done removed
# cat rama*.txt combined_numbers.txt > ALL.txt
# (,  ), and done removed
str_filename = 'runs/ALL.txt'
copy_numbers <- read.csv(file = str_filename, sep = ',', 
                         header = FALSE, stringsAsFactors=FALSE, na.strings="..")

copy_numbers

####################################
# select unique numbers
####################################
ramanujan_numbers = sqldf("select distinct(V5) as x
                          from copy_numbers
                          order by x ")

####################################
# plot histogram
####################################
hist(log10(as.numeric(ramanujan_numbers$x)), main="Histogram for Ramanujan numbers", 
     xlab="Log10 of Ramanujan numbers", 
     border="black", 
     col="blue", breaks = 100)


hist((as.numeric(ramanujan_numbers$x)), main="Histogram for Ramanujan numbers", 
     xlab="Ramanujan numbers", 
     border="black", 
     col="blue", breaks = 100)


gp2 <- ggplot(ramanujan_numbers, aes(x=x))
gp2 <- gp2 + geom_histogram()#alpha=0.5)
gp2 <- gp2 + xlab("Value of Ramanujan number") + ylab("Frequency")
# gp <- gp + facet_wrap(histology~.)
# gp2 <- gp2 + facet_grid(age~.)
gp2
ggsave(filename = "hist_ramanujan_numbers.eps", gp2,
       device = "eps")#,  useDingbats=FALSE)


gp2 <- ggplot(ramanujan_numbers, aes(x=log10(x)))
gp2 <- gp2 + geom_histogram()#alpha=0.5)
gp2 <- gp2 + xlab("log 10 of value of Ramanujan number") + ylab("Frequency")
# gp <- gp + facet_wrap(histology~.)
# gp2 <- gp2 + facet_grid(age~.)
gp2
ggsave(filename = "hist_ramanujan_numbers_log10.eps", gp2,
       device = "eps")#,  useDingbats=FALSE)


