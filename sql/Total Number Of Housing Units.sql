select year,sum(south + west + midwest + northeast) AS total_housing_units
from [dbo].[housing_units_completed_us]

group by year
order by year asc;