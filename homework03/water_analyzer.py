import json
import requests

safe_threshold = 1.0
decay_factor = 0.02

from typing import List 

def calc_turb(turbitdata: List[dict], calCon: str, detec: str) -> float:
    """
    This function does calculates the turbidity using the calibration constant and the degree detector            
    Args: List, Calibration Constant, Degree detector
    Returns: the average turbidity
   
    """
    
    totTurb = 0
    for i in range(1,6):
        totTurb += turbitdata[-i][calCon] * turbitdata[-i][detec]
    return (totTurb/5)

def calc_min_time(currTurb) -> float:
    """
    This function does determines if the turbidity is within the threshold and then finds the time it takes to get the turbidity below the threshold
    Args: the average trubidity found in the first function, or the "currTurb"
    Returns: 0 or the minimum time it takes to get the turbidirty under the threshold

    """
    if currTurb <= safe_threshold:
        return 0
    else:
        return ((currTurb - safe_threshold) / decay_factor)

def main():
    # import data from the website

    data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')

    turbitdata = data.json()

    currTurb = calc_turb(turbitdata['turbidity_data'], 'calibration_constant', 'detector_current')

    print("The average turbidity based on the most recent five measurements is ", currTurb, " NTU")

    if currTurb <= safe_threshold:
        print("Info: The turbidity is below the safe threshold.")
    else:
        print("Warning: The turbidity is above the safe threshold.")

    miniTime = calc_min_time(currTurb)
    print("The minimum time for the turbidity to fall below the safe threshold is ", miniTime, " hours!")


if __name__ == '__main__':
        main()
