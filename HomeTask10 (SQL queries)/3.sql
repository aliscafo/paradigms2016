SELECT City.Name 
FROM City
INNER JOIN Country ON Country.Code = City.CountryCode
INNER JOIN Capital ON City.Id = Capital.CityId
WHERE Country.Name = 'Malaysia';

