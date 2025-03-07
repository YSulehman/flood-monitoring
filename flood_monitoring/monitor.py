import requests
import pandas as pd
from datetime import datetime, timedelta


class FloodMonitor:
    # root path for the available APIs
    root_pth = 'https://environment.data.gov.uk/flood-monitoring'

    # valid measurements
    valid_measurments = ('water-level', 'wind', 'flow', 'temperature')
    def __init__(self, town: str, measurement: str):
        # check if the measurement is a string
        if type(measurement) != str:
            raise ValueError('measurement must be a string')
        else:
            if measurement not in self.valid_measurments:
                raise ValueError('Invalid measurement')
            else:
                # assign measurement appropriately
                if measurement == 'water-level':
                    self.measurement = 'Water Level'
                elif measurement == 'flow':
                    self.measurement = 'Flow'
                elif measurement == 'wind':
                    self.measurement = 'Wind'
                elif measurement == 'temperature':
                    self.measurement = 'Temperature'
        
        # check if the town is a string
        if type(town) != str:
            raise ValueError('town must be a string')
        else:
            self.town = town

        # get the current date 
        self.end_date = datetime.today().strftime('%Y-%m-%d')
        self.start_date = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
        # print(f'todays date is {self.current_date} and yesterday it was {self.yesterday_date}')
        self.reading_parameters = {'startdate': self.start_date,
                                   'enddate': self.end_date}

        # initialise parameters to be used in the API
        self.parameters = {
            'parameterName': self.measurement,
            'town': self.town
        }
    
    def perform_monitoring(self, parameters: dict):
        # url for all the stations
        # self.stations_pth = os.path.join(self.root_pth, 'id/stations') # may not work on windows (works on linux)
        self.stations_pth = f"{self.root_pth}/id/stations"


        response = requests.get(self.stations_pth, params=parameters)
        # if request not good print error code
        if response.status_code != 200:
            raise ValueError(f'Error: {response.status_code}')
        else:
            data = response.json()
            # list of dictionaries 
            self.stations = data['items']
            # print a message if there are no stations based on the given parameters
            if len(self.stations) == 0:
                print('No stations found based on the given parameters')
            else:
                print('Stations found based on the given parameters')
                # just for testing only getting first... either need additional filters or if more than one then just select one?
                self.individual_station_pth = self.stations[0]['@id']
                print(self.individual_station_pth)

                # get all reading for selected station within last day
                readings_url = f'{self.individual_station_pth}/readings'

                readings_response = requests.get(readings_url, params=self.reading_parameters)

                reading_data = readings_response.json()

                # get list corresponding to items key
                items = reading_data['items']

                print(len(items))
                # for x in items:
                #     print(x['value'])

                # plot values vs date
                

    def _plot_line_graph(self):
        pass

if __name__ == "__main__":
    fm = FloodMonitor('Netherside Hall', 'flow')

    fm.perform_monitoring(fm.parameters)

