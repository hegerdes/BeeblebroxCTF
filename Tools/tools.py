import os


#Need sudo privileges
def checkSudo():
    if(os.getuid() != 0):
	    print("Sorry. This script requires sudo privledges")
	    exit(1)

#Make Skrip work form any caller location
def chechandsetCWD():
    if(__file__ != 'deployCTF.py'):
        os.chdir(os.path.dirname(__file__))


#Check output of subprocess
def check_output(pout,debug=False):
	sub_out, sub_err = pout.communicate()
	if(len(sub_err.decode()) > 1):
		print(sub_err.decode())
		return(False)
	if(debug and len(sub_out.decode()) > 1):
		print(sub_out.decode())
	return(True)