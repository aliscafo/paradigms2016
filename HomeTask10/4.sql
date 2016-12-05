SELECT Country.Name, count(City.Name) AS Num
FROM Country LEFT OUTER JOIN City
ON Country.Code = City.CountryCode AND City.Population >= 1000000
GROUP BY Country.Name
ORDER BY Num DESC, Country.Name;

