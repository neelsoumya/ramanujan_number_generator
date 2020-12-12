###############################################################################################################################################
###############################################################################################################################################
# Program name - ramanujan_test_v1.py
#
# Author - Soumya Banerjee
# Creation date - Sept 16th 2014
# Website - https://sites.google.com/site/neelsoumya/
#
# Description -   
# Calculate Ramanujan numbers - numbers that can be expressed as the sum of two cubes
#   in two different ways i.e. a^3 + b^3 = c^3 + d^3 where a != c, a != d, b != c, b != d
#   1729 = 12^3 + 1^3 = 10^3 + 9^3
#
#   Input - Maximum value of each constituent number
#
#   Output -
#           ramanujan_numbers_list.txt
#       
#
#   Example - nohup python ramanujan_test_v1.py
#
#  Change History -
#                   16th Sept 2014 - Creation by Soumya Banerjee
#                   18th Sept 2014 - Modified by Soumya Banerjee
#                                       redundant comments removed
#                   13th Nov  2014 - Modified by Soumya Banerjee
#                                       lower limit added (iLowerLimit)
#
###############################################################################################################################################
###############################################################################################################################################

iLowerLimit = 1
iUpperLimit = 1000

output_file_final = 'ramanujan_numbers_list.txt'
output_file_ptr_final  = open(output_file_final, 'w')

for iInner_1 in range(iLowerLimit, iUpperLimit):
    for iInner_2 in range(iInner_1 + 1, iUpperLimit):
        for iInner_3 in range(iLowerLimit, iUpperLimit):
            for iInner_4 in range(iInner_3 + 1, iUpperLimit):
                #if iInner_1**3 + iInner_2**3 == iInner_3**3 + iInner_4**3: #and iInner_1 != iInner_3 and iInner_2 != iInner_4 and iInner_1 != iInner_4 and iInner_2 != iInner_3:
                if iInner_1**3 + iInner_2**3 == iInner_3**3 + iInner_4**3 and iInner_2 != iInner_4 and iInner_1 != iInner_4 and iInner_2 != iInner_3:
                    output_file_ptr_final.write(str(iInner_1) + '\t' + str(iInner_2) + '\t' + str(iInner_3) + '\t' + str(iInner_4) + '\t' + str(iInner_1**3 + iInner_2**3) + '\n')                    
                    #print(iInner_1,iInner_2,iInner_3,iInner_4,iInner_1**3 + iInner_2**3)

print('Completed')
output_file_ptr_final.close()



if __name__ == "__main__":
    import sys
    
