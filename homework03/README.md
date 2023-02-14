Homework 3 - The World Has Turned and Left Me Turbid, Analyzing water data to 
determine the turbidty

In this homework set folder, two scripts were created to use data from an online 
source to further analyze the safety of water (the source can be referenced with this link:
 https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). 
The objective of this project was to first extract information from an online data base to then manipulate mathematically.
Then the other file should then test the script for any errors.

In the script, water analysis, the program first extracts data form an online 
data-base and then runs the following data into two functions that helps to find the average turbidity and the minimum amount of time required to push the turbidity 
within the safe threshold. In the second script, test water analysis, it uses pytest
to test its capabilities and accuracy.

In order to run the following files:
 
 1) Compile the "water_analysis.py" script in the command line by using the lines
	"python3 water_analysis.py"
 2) In the command line, there should be a message describing the turbidity

To test the file:
 
 1) Compile the "test_water_analysis.py" script in the command line by using the
	lines "pytest test_water_analysis.py"
 2) In the command line, the computer should give a detailed message of an error
	or if the expected value was met

Let's discuss what the results mean! If the message tells you that the turbidity is
above the safe trheshold, that means it needs to take some time to drop into the 
safe threshold (this means that the time should be communicated as well). If the
message tells you that the turbidity is below the safe threshold, that means that
there is no need to worry and that the water is safe (this means that the time is 
equal to zero because it is already in the needed range).

Thank you for grading my homework! 
