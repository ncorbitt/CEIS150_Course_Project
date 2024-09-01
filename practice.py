riders_per_ride = 3  # Num riders per ride to dispatch
line = ['etan','atan','btan']  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

for rider in range(0,riders_per_ride):
    print(f'rider->{rider}')
    dispatched = line.pop(rider)
    print(f'Dispatched {dispatched}')