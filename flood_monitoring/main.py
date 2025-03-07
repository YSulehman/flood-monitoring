import argparse
from .monitor import FloodMonitor

def main(args):
    # flood monitor agruments
    flood_monitor_args = {
        'town': args.town,
        'measurement': args.measurement
    }

    # make an instance of the FloodMonitor class
    fm = FloodMonitor(**flood_monitor_args)

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    # arguments to provide control over measurement station
    parser.add_argument('town', type=str, help='The town to monitor')
    parser.add_argument('measurement', type=str, choices=['water-level', 'wind', 'flow', 'temperature'], help='The measurement to monitor')