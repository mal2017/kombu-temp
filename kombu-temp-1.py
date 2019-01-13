import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# sensors live here
base_dir = '/sys/bus/w1/devices/'

# will only work for one probe for now
device_folder = glob.glob(base_dir + '28*')[0]

# actual text file the probe writes to
device_file = device_folder + '/w1_slave'



def read_w1_probe(dev_f):
    with open(dev_f, 'r') as f:
	lines = f.readlines()
    return lines


def parse_temp():
	raw = read_w1_probe(device_file)
	while raw[0].strip()[-3:] != 'YES':
		time.sleep(0.5)
		raw = read_w1_probe(device_file
	)

	l1_temp_idx = raw[1].find('t=')

	if l1_temp_idx != -1:
		t = raw[1][l1_temp_idx + 2:]
		fahr = 32+((float(t)/1000)*(9.0/5.0))
	return fahr

while True:
	print(parse_temp())
	time.sleep(1)
