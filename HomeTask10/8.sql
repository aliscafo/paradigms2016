SELECT Name, Population, SurfaceArea FROM Country WHERE Code IN	
	(SELECT Capital.CountryCode
	FROM Capital 
	INNER JOIN City AS NotCapital ON Capital.CountryCode = NotCapital.CountryCode
	INNER JOIN City CapitalPop ON CapitalPop.Id = Capital.CityId
	WHERE NotCapital.Population > CapitalPop.Population
	GROUP BY Capital.CountryCode)
ORDER BY CAST(Population AS FLOAT) / SurfaceArea DESC, Name;
