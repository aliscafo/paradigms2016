SELECT City.Name, City.Population, Country.Population 
FROM City INNER JOIN Country
ON City.CountryCode = Country.Code
ORDER BY CAST(City.Population AS FLOAT) / CAST(Country.Population AS FLOAT) DESC, City.Name DESC
LIMIT 20;

