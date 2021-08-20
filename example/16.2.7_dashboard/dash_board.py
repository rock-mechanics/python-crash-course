#!/usr/bin/env python3

import os
import re

p = r'.*\.svg'
with open('dash_board.html', 'w') as f : 
    f.write('<html><head><title>Closing Price BTC DashBoard</title></head><body>\n')
    for svg in os.listdir() : 
        if re.match(p, svg) : 
            f.write('   <object type="image/svg+xml" data="{}" height = 500></object>\n'.format(svg))

    f.write('</body></html>')
