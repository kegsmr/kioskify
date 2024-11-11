import subprocess
import sys
import time
from pathlib import Path


exec_path = Path(sys.argv[1])
exec_file = exec_path.name


def main():
	subprocess.Popen(exec_path)
	while process_exists(exec_file):
		time.sleep(.1)
	subprocess.run("shutdown -l")


def process_exists(process_name):
	call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
	output = subprocess.check_output(call, shell=True).decode()
	last_line = output.strip().split('\r\n')[-1]
	return last_line.lower().startswith(process_name.lower())
	

if __name__ ==  "__main__":
	main()