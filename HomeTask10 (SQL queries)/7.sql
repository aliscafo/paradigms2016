SELECT Country.Name 
FROM Country LEFT OUTER JOIN City
ON Country.Code == City.CountryCode
GROUP BY Country.Name
HAVING Country.Population - SUM(City.Population) > SUM(City.Population);
