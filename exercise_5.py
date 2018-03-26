# David Crowley g00364706

#Write a Python script that reads the Iris data set in and 
# prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width,
#  and these values should have the decimal places aligned, with a space between the columns.

# open file iris.data in read mode (for text which is the default anyway)


with open('iris.data', 'rt') as irisdata:
    # for each line in the data set
    for line in irisdata:
        # print(line)
        # split the line and store it
        splitline = line.split(",")
        # print out details needed with the added string details to show the user the details needed
        print("Sepal Length: " + splitline[0] + " " + "Sepal Width: " + splitline[1] + " " + "Petal Length: " + splitline[2] + " "+ "Petal Width: " + splitline[3]) 
# close the file       
irisdata.close()
