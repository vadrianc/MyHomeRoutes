import argparse

from track import Track
from sampler import Sampler
from plotter import Plotter

def gather(interval):
    track = Track('in\\key.key', 'in\\from.txt', 'in\\to.txt', True)
    sampler = Sampler()
    sampler.gather(track.gather_directions_data, interval)

def plot(result, routes):
    plotter = Plotter(result, routes)
    plotter.draw()

def get_cmd_parser():
    parser = argparse.ArgumentParser(description='Gather and/or plot google maps real time data for driving between locations')
    parser.add_argument('-g', '--gather', action='store_true', help='Gather data at specified interval')
    parser.add_argument('-i', '--interval', help='Regular time interval given in seconds, used to gather data. If not specified, default is 3600 seconds')
    parser.add_argument('-p', '--plot', help='CSV input file containing the routes to plot')
    parser.add_argument('-r', '--result', help='CSV result file used for plotting')
    return parser

def handle_args():
    parser = get_cmd_parser()
    args = parser.parse_args()

    if args.gather:
        interval = 3600
        if args.interval:
            interval = int(args.interval)
        gather(interval)
    elif args.plot and args.result:
        plot(args.result, args.plot)
    else:
        parser.print_help()

def main(): 
    try:
        handle_args()
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)
        print('Unexpected error occured')
  
if __name__=="__main__": 
    main()