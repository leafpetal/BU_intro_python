#
# open_close_file.py - Problem Set 6, Problem 1
#
# Open, process, and close a file
#

# 1790,1,Philadelphia,PA,44.1 ...

# helper function
def helper(city, st_abb, filename):
    count = 0
    file = open(str(filename))
    for line in file:
        line = line[:-1] # to get rid of \n
        fields = line.split(',') # fields = [1790, 1, Philadelphia, PA, 44.1]
        #print(fields)
        pop = float(fields[-1])*1000
        #print(pop)
        if fields[2] == city and fields[3] == st_abb:
            count += 1
            print(fields[0] + '\t' + fields[1] + \
                  '\t' + format(int(pop), '10,d'))
    if count == 0:
        print("no results found for", city + ', ' + st_abb)
        
    file.close()

def main():
    """ the main user-interaction loop
    """
    filename = str(input('Enter the name of data file: ')) # cities.txt
    print()
    #file = open(str(filename))
    #count = 0
    
    while True: 
        count = 0
        city = str(input('city: '))
        
        if city == 'quit':
            break
        else:
            st_abb = str(input('state abbreviation: '))
            helper(city, st_abb, filename)
    #file.close()
#main()
