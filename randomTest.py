import ecdsa 
import os 
from ecdsa.util import string_to_number , number_to_string 

def random_secret(): 
	convert_to_int = lambda array:int( "".join( array ).encode( "hex" ),16 )
	
	# Collect 256 bits of random data from the OS's cryptographically secure random generator 

	byte_array = os.urandom(32)

	return convert_to_int(byte_array)
	
secret = random_secret()
print ("Secret: " , secret)

