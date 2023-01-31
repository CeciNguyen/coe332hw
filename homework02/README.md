No one JSON - Homework 02, Investigating Meteorite Landing Sites

In this homework set folder, two scripts were crafted to simulate and analyze meteorite landings on Mars from the perspective of an operator of a robotic vehicle. 
The objective of this project was to first simulate an interactive enviornment for our robot to discover by generating different and random meteroite landing 
coordinates. Then the robot would properly analyze the time it takes to go from each site and "sample" each meteorite.

In the script, generate sites, the program helps to generate five unique sites with randomized coordinates and compositions. The script then develops a JSON file
that gets analyzed by the next script, calculate trip. In calculate trip, the script determines the total time the robot takes to run to every site and sample the 
enviornment. In order to do so, the script uses a variety of functions to determine the distance, the time it takes to travel to each site, and how long each 
sample takes based on its composition.

How do you run the code? Great question!

To properly run the code:
  1) Compile the "generate_ sites.py" script in the command line
  2) In the command line, type "ls" to make sure a JSON file was generated. The file should be called "MarsSyrtisMajor.json".
  3) Once you can confirm a JSON file was created, compile the "calculate_trip.py" script.
  4) You should see an output of each leg, which is the segment traveled between each point/ site.

Now, what does the output mean? Well, each leg (segment) will have its own seperate travel time and sample time. This tells you how long the robot takes to travel 
from one site to the next and how long the robot takes to sample based on the composition of the meteorite.

Thank you for grading my homework :)!     
