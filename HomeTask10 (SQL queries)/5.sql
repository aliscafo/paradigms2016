SELECT GovernmentForm, SUM(SurfaceArea) 
FROM Country
GROUP BY GovernmentForm
ORDER BY SUM(SurfaceArea) DESC
LIMIT 1;
