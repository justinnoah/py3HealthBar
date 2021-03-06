# v0.3 Displays 1 Hash Mark for every five minute increment you have been logged in.
# Resets after you have logged in.
# All values are static
# Written by Elijah Voigt and Lucy Wyman

from time import time
import subprocess

global time 
time_t = time()
TIMEOUT = 1

class Py3status:

    def test(self, i3status_output_json, i3status_config):
        l_time = time()
        delta = l_time - time_t
        delta = int(delta)

        var = "#"

        x = delta/300
        x = int(x)
        for i in range (0,x):
            var += str("#")

        condition = (x < 4)

        status = '{}'.format(var)

        response = {'name': 'healthbar', 'full_text': status}
        response['cached_until'] = TIMEOUT 

        if condition:
            response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_bad']

        if (len(var)> 12):
            global time_t 
            time_t = time()
            subprocess.call('i3lock')	

        return (0, response)

