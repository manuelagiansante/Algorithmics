# import the neighbours function
from neighbours import neighbours_func

def breadth_search(city: str, country: str, k: int, d: str, s: str):
    '''
    The function runs a breadth first search for k steps. So starting from the input city it will re-run the algorithm
    for all the cities found in the kth step. It uses the neighbours_func to source the cities from the sql to build the
    neighbour sets.
    The cities reachable within each step are printed in lists as the function builds the respective N(ci) sets.
    :param city: The name of the city we want to start our search from, our tree root as a string;
    :param country: Country the city we are starting the search from is in;
    :param k: Is the number of "steps" for which the search is performed;
    :param d: The parameter for the distance within which the starting city and the next city can be considered to be neighbours;
    :param s: The parameter for the distance that categorizes neighbours for cities on the same sea;
    :return: The function prints the lists of reachable cities reachable within the stated number of steps.
    '''
    checked_cities = set()               # initialising set for the checked/visited cities
    checked_cities.add((city, country))  # to the checked cities we add the starting city we input
    queue = []                           # list that will contain all the cities to be "explored"


    for i in range(1,k+1):  # Iterate the search process for every number of steps up to k number of steps
        if i == 1:          # search at step one
            first_step = neighbours_func(city, country, s, d) # List of tuples where we store N(ci) within 1 step
            print(str(i)," Step: \n",first_step)              # Print the N(ci) within 1 step
            checked_cities.update(first_step)                 # Keep track of the already visited cities, so to not encounter them again and go "backwards" in our search
            queue.extend(first_step)                          # The search will be conducted from the output cities in the next step
        else:
            to_check = []                                     # object where we will store the cities that will later on be added to the queue
            while len(queue) > 0:                             # perform the search for every city reached in the previous step
                removed = queue.pop(0)                        # to store the first city in the queue
                nth_step = neighbours_func(removed[0], removed[1], s, d)  # Build N(ci) for the removed city at the corresponding nth step
                for x in nth_step:                                        # iterating over the cities in N(ci) for the nth step
                    if x not in checked_cities and len(x) == 2:           # If it has not been visited yet and it is of the right length
                        to_check.append(x)                                # to update the queue
                        checked_cities.add(x)                             # Record the ones you checked
            print()
            print(str(i), "Steps: \n",to_check)                           # the cities to check in the next step are also the cities reachable at the current step
            queue.extend(to_check)                                        # update the queue










def main():
    city = "Geneva"
    country = "CH"
    s = "4"
    d = "2"
    k = 5
    print(breadth_search(city, country, k, d, s))

if __name__ == "__main__":
    main()


