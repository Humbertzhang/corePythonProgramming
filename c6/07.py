
#input a num in string type
num_str = raw_input("Enter a number:")

#change the string into int
num_num = int(num_str)

#make a list like[1,2,3,...num_num]
fac_list = range(1,num_num+1)
print "Before:",fac_list

#index i = 0
i=0

#while i < num_num
while i<len(fac_list):
    
    #if the number can be divided completely by the num in the list,delete the num in the list
    if num_num%fac_list[i] == 0:
        del fac_list[i]

    #
    i = i + 1

print "After:",fac_list