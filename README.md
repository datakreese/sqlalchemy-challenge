# SQLalchemy Ecology Analysis
## Overview
Using Sqlalchemy and Flask, this project queries the database for weather stations in Hawaii and returns the relevant information.

- Station data includes station ID, name, coordinate location, and elevation.
- Weather information includes station ID, date, precipitation, and temperature.

Matplotlib and pandas libraries are used for primary visualizations.

## Results
Precipitation Summary:
- Max 6.7 inches with a min 0.0
- Mean of 0.18 inches and standard deviation of 0.46 inches

Stations Summary:
- ID USC00519281 logged max entries with 2772 data points
- In terms of temperature the station logged min of 54°F, max 85°F, and mean 71.67°F.

## Further Analysis
- A time series study (STL) of previous decades would provide better context for any skewing tendencies and influence agriculture, water management, and biodiversity studies.
- Run a Pearson Correlation test to identify any relationships between temperature and precipitation, highlighting one dimension of climate change.
- Visualize both temp and precip with heat mapping to inform land use planning and resource management.

## Sources 
Flask code fine tuned in collaboration with Amman Shearhad. 
