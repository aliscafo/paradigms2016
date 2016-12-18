SELECT Country.Name, Country.Population, Country.SurfaceArea 	
FROM Capital 
INNER JOIN Country ON Country.Code = Capital.CountryCode
INNER JOIN City AS NotCapital ON Capital.CountryCode = NotCapital.CountryCode
INNER JOIN City CapitalPop ON CapitalPop.Id = Capital.CityId
WHERE NotCapital.Population > CapitalPop.Population
GROUP BY Capital.CountryCode
ORDER BY CAST(Country.Population AS FLOAT) / Country.SurfaceArea DESC, Country.Name;

