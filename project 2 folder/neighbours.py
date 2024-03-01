
from urllib.request import urlopen
from urllib.parse import quote, urlencode


def neighbours_func(city: str, country: str, s: str, d : str) -> set[str, str] :
    '''
    The function queries the mondial sql database. For a given city name it  builds a neighbour N(ci) for it, the items in N(ci) fulfill a set of conditions.
    The conditions stated in the query are discussed in the query py file.
    Resources: Course material on MySQL queries and the assignment PDF.

    :param city: The name of the city we want to build the "neighbour" N(ci) for;
    :param country: The name of the country the city is in, it is used a second identificator, because cities can have the same name;
    :param s: The maximum distance within which cities that are on the same city as the input city can be considered to be within the neighbour N(ci);
    :param d: The maximum distance used to categorize cities as neighbours of the input cities, when all others conditions are not fulfilled.
    :return: The function returns N(ci) in the form of a list of sets, where the city name and country code are stated.
    '''
    q = "SELECT c.Name, c.Country " \
        "FROM City c " \
        "LEFT JOIN located l ON c.Name = l.City " \
        "WHERE NOT (c.Name = '"+ city + "')" \
                    "AND ((l.River in (SELECT l2.River FROM located l2 WHERE l2.City = '" + city + "'AND l2.Country='"+ country + "'))" \
                            "OR  (l.Lake in (SELECT l3.Lake FROM located l3 WHERE l3.City = '"+ city +"' AND l3.Country='"+ country + "'))" \
                            "OR (c.Province in (SELECT c1.Province FROM City c1 WHERE c1.Name = '"+ city +"'AND c1.Country='"+ country + "'))" \
                            "OR ((l.Sea in (SELECT l4.Sea FROM located l4 WHERE l4.City = '"+ city + "'AND l4.Country='"+ country + "')) " \
                                    "AND ABS(c.Latitude - (SELECT c2.Latitude FROM City c2 WHERE c2.Name = '" + city +"' AND c2.Country='"+ country + "')) " \
                                                                      "+ ABS(c.Longitude - (SELECT c2.Longitude FROM City c2 WHERE c2.Name = '"+ city +"'AND c2.Country='"+ country + "')) < "+ s +")" \
                            "OR (ABS(c.Latitude - (SELECT c2.Latitude FROM City c2 WHERE c2.Name = '"+ city +"'AND c2.Country='"+ country + "')) " \
                                                                      "+ ABS(c.Longitude - (SELECT c2.Longitude FROM City c2 WHERE c2.Name = '" + city + "' AND c2.Country='"+ country + "'))) < " + d +")"
    eq = quote(q) # formats the sql query
    url = "http://kr.unige.ch/phpmyadmin/query.php?db=mondial&sql=" + eq # creates the url
    query_results = urlopen(url)                                         # object to store the retrieved raw data from the http server
    city_code = set()                                                    # initialises the couple ot city name and country code under the form of a set
    for line in query_results:                                           # iterating over every line of the results/response
        string_line = line.decode('utf-8').rstrip() # decoding the response text and stripping it of trailing chacraters, meaning any charcaters at the end of the string
        columns = string_line.split("\t")           # unashable type list, diving the lines of strings into columns
        pairs = tuple(columns)                      # making a tuple, to store the city and country variables into one item
        city_code.add(pairs)                        #add each pair of city and country to the previously initialised set
    return list(city_code)                          # returns a list of 2 variables sets





def main():
    city ="Geneva"
    country = "CH"
    s = "4"
    d = "2"
    print(neighbours_func(city, country, s, d))

if __name__=="__main__":
    main()
