import os
import requests

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

        # initialise parameters to be used in the API
        self.parameters = {
            'parameter': self.measurement,
            'town': self.town
        }
    
    def get_data(self, parameters: dict):
        # url for all the stations
        self.stations_pth = os.path.join(self.root_pth, 'id/stations')


        response = requests.get(self.stations_pth, params=parameters)
        if response.status_code != 200:
            raise ValueError(f'Error: {response.status_code}')
        else:
            self.stations = response.json()
            # print a message if there are no stations based on the given parameters
            if len(self.stations['items']) == 0:
                print('No stations found based on the given parameters')
            else:
                pass
                print('Stations found based on the given parameters')
                # for station in self.stations['items']:
                #     print(f"Station Name: {station['label']}")
                #     print(f"Station ID: {station['notation']}")
                #     print(f"Station URL: {station['self']}")
                #     print('\n')

    def _plot_line_graph(self):
        pass

if __name__ == "__main__":
    fm = FloodMonitor('Liverpool', 'flow')

    fm.get_data(fm.parameters)

