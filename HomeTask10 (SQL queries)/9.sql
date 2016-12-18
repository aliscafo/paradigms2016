SELECT St.Year, MIN(En.Year), Country.Name, (En.Rate - St.Rate) / (En.Year - St.Year)
FROM Country 
INNER JOIN LiteracyRate AS St ON St.CountryCode = Country.Code
INNER JOIN LiteracyRate AS En ON En.CountryCode = Country.Code
WHERE St.Year < En.Year
GROUP BY Country.Name, St.Year
ORDER BY (En.Rate - St.Rate) / (En.Year - St.Year) DESC;

