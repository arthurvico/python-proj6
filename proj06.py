##############################################################################
#       CSE 231 Project #6
#       In this project I will be given an excel file with different
#       census data. I will process this data and create an organized
#       list with a graph.
#       1) I will open the file using the open_file function
#       2) I will use the read function to format the inputs into
#       organized lists and tuples
#       3) I will use these lists and tuples and format a chart of all info
##############################################################################




import pylab   # for plotting

def open_file():
    '''This function will be used to open a given file and make sure that it is a valid file'''
    #Create a try and except error
    while True:
        #While this is true, we can open the file
        try:
            #try to open the file here
            file_name = input("Enter a file name: ")
            file_open = open(file_name, "r")
            #We return the opened file
            return file_open
        #If this is false, We return an error and promt for a new file
        except:
            #if error, try again
            print("Error. Please try again.")

def find_index(header_list,s):
    '''This function will return the column of the input string'''
    #Create an enumerate for loop, to get the index of the desired column
    for i,ch in enumerate(header_list):
        if ch == s:
            return i

def read_2016_file(fp):
    '''This function will return an organized list of tuples with all of the states and their data'''
    #Strip the two first header, for later formating
    header = fp.readline()
    header2 = fp.readline()
    #Make the first header a list
    header_list = header.split(',')
    #Create a final_list for later
    final_list = []
    #Use a for each line loop
    for line in fp:
        #Create an empty string
        str_each_state = ''
        #Create an empty list
        list_each_state_full = []
        #Split each line in a list
        line_split = line.split(',')
        #Initialize two values
        ratio_nat = 0
        ratio_non = 0
        #Create an empty list
        final_list_sorted = []
        #Create a list of the wanted columns
        columns_wanted = ["GEO.display-label", "EST_VC197", "EST_VC201", "EST_VC211"]
        #Create a for loop to find the index of each column
        for s in columns_wanted:
            #Call the find_index function and store the column value
            position = find_index(header_list,s)
            #Create a string for each state of the different wanted data, using the position
            str_each_state += line_split[position]+","
            #Split that string into a list
            list_each_state = str_each_state.split(",")
        #Remove the last item in that list as it is empty
        list_each_state.pop()
        #Calculate the total citizen amount
        total_citizen = int(int(list_each_state[1])+int(list_each_state[2])+int(list_each_state[3]))
        #Calculate the ratio of natural citizen
        ratio_nat = int(list_each_state[2])/total_citizen
        #Calculate the ratio of non citizen
        ratio_non = int(list_each_state[3])/total_citizen
        #These next lines will be to create a list of all of our data
        list_each_state_full.append(list_each_state[0])
        list_each_state_full.append(int(list_each_state[1]))
        list_each_state_full.append(int(list_each_state[2]))
        list_each_state_full.append(ratio_nat)
        list_each_state_full.append(int(list_each_state[3]))
        list_each_state_full.append(ratio_non)
        #Now make this list a tuple
        tuple_list = tuple(list_each_state_full)
        #We then create a list of all of the tuples
        final_list.append(tuple_list)
        from operator import itemgetter
        #Here we sort them using the last digit of each tuple
        final_list_sorted = sorted(final_list,key=itemgetter(5))
    return(final_list_sorted)
            
        
def read_2000_file(fp2):
    '''This function will return an organized list of tuples with all of the states and heir data'''
    #Strip both headers away
    header = fp2.readline()
    header2 = fp2.readline()
    #Create a list of the first header
    header_list = header.split(',')
    #Create a for loop for each line in the file
    for line in fp2:
        #Create an empty string
        str_each_state = ''
        #Create an empty list
        list_each_state_full = []
        #Split each line at a comma
        line_split = line.split(',')
        #Create an empty list
        final_list_sorted = []
        #Create a list of all the wanted columns
        columns_wanted = ["HC01_VC02","HC01_VC03","HC01_VC05","HC01_VC06"]
        #Create a for loop for each of the items in the wanted columns
        for s in columns_wanted:
            #Use the find_index function to collect the index of each wanted column
            position = find_index(header_list,s)
            #Add each desired item to our empty string using our calculated position
            str_each_state += line_split[position]+","
            #Create a list split at each comma
            list_each_state = str_each_state.split(",")
        #Remove the last item as it is empty
        list_each_state.pop()
        #Calculate the number of total citizen
        total_citizen = int(int(list_each_state[1])+int(list_each_state[2])+int(list_each_state[3]))
        #These next lines are to create a list of each calculated item
        list_each_state_full.append(total_citizen)
        list_each_state_full.append(int(list_each_state[1]))
        list_each_state_full.append(int(list_each_state[2]))
        list_each_state_full.append(int(list_each_state[3]))
        #This line is to change the list into a tuple
        tuple_list = tuple(list_each_state_full)
    return (tuple_list)
def calc_totals(data_sorted):
    '''This function will take the list from the 2016 data function and return
    a tuple of total values'''
    #Set some initial values
    total_native = 0
    total_naturalized = 0
    total_noncit = 0
    total_res = 0
    total_list = []
    #Create a for loop for each item in the 2016 file read function (each tuple)
    for item in data_sorted:
        #Add the total amount of natives, naturalized and non-citizens
        total_native += item[1]
        total_naturalized += item[2]
        total_noncit += item[4]
        #Calculate the total amount of citizens
        total_res = total_native + total_naturalized +total_noncit
    #Create a list with each item calculated
    total_list.append(total_native)
    total_list.append(total_naturalized)
    total_list.append(total_noncit)
    total_list.append(total_res)
    #Make that list a tuple
    total = tuple(total_list)
    return (total)

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):
    '''This function will take 6 values as an argument and return them organized into 1 tuple of 3 lists '''
    #Create 3 different lists with inputed data
    list1 = [native_2000,native_2016]
    list2 = [naturalized_2000,naturalized_2016]
    list3 = [non_citizen_2000,non_citizen_2016]
    #Take each list and create a tuple with it
    total_tuple = (list1,list2,list3)
    return (total_tuple)

def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(2)   # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color and a label
    pylab.bar(X, native_list, color = 'b', width = 0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color = 'g', width = 0.25, label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color = 'r', width = 0.25,label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000","2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    #pylab.savefig("plot.png")

def main():    
    '''Insert DocString here.'''
    #Call the open file function
    fp = open_file()
    #Set a value equal to the read_2016_function to use in another functions
    data_sorted = read_2016_file(fp)
    #Call the open file function again
    fp2 = open_file()
    #Use the read_2000_file function to extract some numbers
    read_2000 = read_2000_file(fp2)
    #Calculate the total populations
    sorted_2016 = calc_totals(data_sorted)
    #Set 6 values from each rfead functions to use in my make_lists_for_plot function
    native_2000 = read_2000[1]
    naturalized_2000 = read_2000[2]
    non_citizen_2000 = read_2000 [3]
    native_2016 = sorted_2016[0]
    naturalized_2016 = sorted_2016[1]
    non_citizen_2016 = sorted_2016[2]
    #Call the make_lists_for_plot function
    end_list = make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016)
    #Create 3 more variables to use in my function
    native_list = end_list[0]
    naturalized_list = end_list [1]
    non_citizen_list = end_list[2]
    #Print format a header
    print("{:>81s}".format("2016 Population: Native, Naturalized, Non-Citizen\n"))
    #Print formate a second header
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format('State','Native','Naturalized','Percent Naturalized','Non-Citizen','Percent Non-Citizen'))
    #Create a for loop for each item in the data_sorted function
    for item in data_sorted:
        item3_mult = item[3]*100
        item5_mult = item[5]*100
        item3_rounded = float(round(item3_mult,1))
        item5_rounded = float(round(item5_mult,1))
        #Print format each line of each state's data
        print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format(str(item[0]),"{:,}".format(item[1]),"{:,}".format(item[2]),str(item3_rounded)+"%","{:,}".format(item[4]),str(item5_rounded)+"%"))
    #Create some values for more string formating, these will be the ones towards the end of the chart
    percent_nat_2016 = ((naturalized_2016)/(naturalized_2016+native_2016+non_citizen_2016))*100
    percent_nat_2000 = ((naturalized_2000)/(naturalized_2000+native_2000+non_citizen_2000))*100
    percent_nat_2016_rounded = float(round(percent_nat_2016,1))
    percent_nat_2000_rounded = float(round(percent_nat_2000,1))
    percent_non_2016 = ((non_citizen_2016)/(naturalized_2016+native_2016+non_citizen_2016))*100
    percent_non_2000 = ((non_citizen_2000)/(naturalized_2000+native_2000+non_citizen_2000))*100
    percent_non_2016_rounded = float(round(percent_non_2016,1))
    percent_non_2000_rounded = float(round(percent_non_2000,1))
    #More print formating
    print("----------------------------------------------------------------------------------------------------------------")
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("Total 2016","{:,}".format(native_2016),"{:,}".format(naturalized_2016),str(percent_nat_2016_rounded)+"%","{:,}".format(non_citizen_2016),str(percent_non_2016_rounded)+"%"))
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("Total 2000","{:,}".format(native_2000),"{:,}".format(naturalized_2000),str(percent_nat_2000_rounded)+"%","{:,}".format(non_citizen_2000),str(percent_non_2000_rounded)+"%"))
    answer = input("Do you want to plot?")
    #create an if statement to ask if the user wants to plot the data.
    if answer == 'yes':
        plot_data(native_list, naturalized_list, non_citizen_list)
    
    
if __name__ == "__main__":
    main()