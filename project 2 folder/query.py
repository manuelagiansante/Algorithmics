'''
    This is the query initially used in the phpmyAdmin interface to get the initial result from which I build the query to insert in the neighbours function:
    We want that the initial search starts from a city from a country.
    The cities that will compose the neighbour N(ci) need to satisfy one this conditions:
    - be on the same river as the given city
    - be on the same lake as the given city
    - be in the same Province
    - be within a minimal distance d
    - be on the same sea but within a given distance s
    The Conditions are stated as a subquery with the IN operator to return multiple values.
    Opted for a LEFT JOIN because of the higher number of rows present in the table City than in the located table.
    Therefore, by including the rows without matching values belonging to the city table provides a larger " graph" to
    conduct the search on.
    Also, added the specification WHERE NOT, to make sure (filter) that when testing the query we are not reaching for the input city again,
    nor when we run the neighbours function on its own. The operators != and <> would have returned a single value.
    Finally, the distances d and s are computed in the query in the following way:
    |ci.latitude−cj.latitude|+|ci.longitude−cj.longitude|
    The computation is done in the query so to not incur into errors due to retrieved NULL values in python.

'''

'''

SELECT c.Name, c.Country, l.River, l.Lake, c.Province
FROM City c
LEFT JOIN located l ON c.Name = l.City
WHERE NOT (c.Name = 'Geneva') AND
      ((l.River in (SELECT l2.River FROM located l2 WHERE l2.City = 'Geneva' AND l2.Country='CH'))
   OR  (l.Lake in (SELECT l3.Lake FROM located l3 WHERE l3.City = 'Geneva'AND l3.Country='CH'))
   OR (c.Province in (SELECT c1.Province FROM City c1 WHERE c1.Name = 'Geneva'AND c1.Country='CH'))
   OR ((l.Sea in (SELECT l4.Sea FROM located l4 WHERE l4.City = 'Geneva'AND l4.Country='CH'))
        AND ABS(c.Latitude - (SELECT c2.Latitude FROM City c2 WHERE c2.Name = 'Geneva' AND c2.Country='CH')) + ABS(c.Longitude - (SELECT c2.Longitude FROM City c2 WHERE c2.Name = 'Geneva' AND c2.Country='CH')) < 4)
       OR (ABS(c.Latitude - (SELECT c2.Latitude FROM City c2 WHERE c2.Name = 'Geneva' AND c2.Country='CH')) + ABS(c.Longitude - (SELECT c2.Longitude FROM City c2 WHERE c2.Name = 'Geneva' AND c2.Country='CH'))) < 2)'''