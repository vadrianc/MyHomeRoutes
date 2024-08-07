from track import Track
from sampler import Sampler
from plotter import Plotter

def main(): 
    plotter = Plotter("results_08_07_2024.csv")
    plotter.draw(["Izvorani", "Piața Victoriei, București",
                  "Bucureștii Noi, Bucharest", "Piața Victoriei, București",
                  "Snagov, 077165", "Piața Victoriei, București",
                  "Otopeni, 075100", "Piața Victoriei, București",
                  "Berceni, 077020", "Piața Victoriei, București"])

    #track = Track('in\\key.key', 'in\\from.txt', 'in\\to.txt', True)
    #track.gather_directions_data()
    #sampler = Sampler()
    #sampler.setup_timers(track.gather_directions_data)
  
if __name__=="__main__": 
    main() 