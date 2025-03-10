# Flood Monitoring

## Example Usage
To select an individual measuremnt station, users can specify:
1. The Town name, 
2. The River name, 
3. The specific measurement of interest (water level, water flow rate, wind direction and speed, or temperature).
4. The specific latitude and longitude coordinates of the region of interest. 
5. A distance d (in kilometers) of all stations falling within d km of the specified latitude and longitude. 

For example, running the command ```python -m flood_monitoring.main  --latitude 51.874767 --longitude -1.740083 --measurement 'Water Level'``` gives the following output:

