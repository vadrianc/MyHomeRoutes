from track import Track
from sampler import Sampler

def main(): 
    track = Track('in\\key.key', 'in\\tracks.csv', True)
    sampler = Sampler()
    sampler.setup_timers(track.gather_directions_data)
  
if __name__=="__main__": 
    main() 