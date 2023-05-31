#Pandas is used as a dataframe to handle Excel files
import pandas as pd
import os

# change the slash from &ldquo;\&rdquo; to &ldquo;/&rdquo;, if you are using Windows devices
input_file_path = "/home/darkstar/Downloads/"
output_file_path = "/home/darkstar/Downloads/"

#create a list to store all the file references of the input folder using the listdir function from the os library.
#To see the contents of a library (like the listdir function, you can use the dir function on the library name).
#Use dir(library_name) to list contents

excel_file_list = os.listdir(input_file_path)

#print all the files stored in the folder, after defining the list

excel_file_list

#Once each file opens, use the append function to start consolidating the data stored in multiple files
#create a new, blank dataframe, to handle the excel file imports

df = pd.DataFrame()

#Run a for loop to loop through each file in the list

for excel_files in excel_file_list:

   #check for .xlsx suffix files only
   if excel_files.endswith(".xlsx"):

       #create a new dataframe to read/open each Excel file from the list of files created above
       df1 = pd.read_excel(input_file_path+excel_files)

       #append each file into the original empty dataframe
       df = df._append(df1)


#transfer final output to an Excel (xlsx) file on the output path 
df.to_excel(output_file_path+"Consolidated_file.xlsx")
