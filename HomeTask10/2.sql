SELECT Country.Name, LiteracyRate.Rate 
FROM Country LEFT OUTER JOIN LiteracyRate 
ON Country.Code == LiteracyRate.CountryCode
GROUP BY Country.Name
HAVING MAX(LiteracyRate.Year)
ORDER BY LiteracyRate.Rate DESC
LIMIT 1;
