from gym.envs.registration import register

register(
    id='grandtour_mit-v0',
    entry_point='gym_grandtour_mit.envs:GrandTour_MIT',
)
