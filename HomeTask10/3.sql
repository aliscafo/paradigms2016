SELECT Name FROM City WHERE Id IN	
	(SELECT CityId FROM Capital WHERE CountryCode IN
		(SELECT Code FROM Country WHERE Name == 'Malaysia'));
