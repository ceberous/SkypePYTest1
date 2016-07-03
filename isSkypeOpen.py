from subprocess import Popen , PIPE , STDOUT
import psutil


def killSkype():

	for proc in psutil.process_iter():
		if proc.name() == "skype":
			proc.kill()

def openSkype():
	Popen('skype')

def check():

	cmd = 'ps aux | grep skype'

	p = Popen( cmd , shell=True , stdin=PIPE , stdout=PIPE , stderr=STDOUT , close_fds=True )

	output = p.stdout.read()
	output = output.split('\n')

	if len(output) > 3:

		x1 = output[0].split(' ')
		
		if x1[-1] == 'skype' and x1[-2] != 'grep':
			return True
		else:
			return False
	else:
		return False
		



