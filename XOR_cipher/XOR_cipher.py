# XOR_cipher
# XOR_unciper = XOR_ciper

def XOR_cipher(file_source_name, file_key_name, mode='cipher'):
	'XOR-encryption'

	file_source = open(file_source_name, 'rt')
	file_key 	= open(file_key_name, 'rt')
	
	if (mode != 'cipher' and mode != 'uncipher'):
		raise ValueError('mode = \'cipher\' or \'uncipher\'') 

	if (mode == 'cipher'):
		out_file_name = file_source_name + '.encr'

	if (mode == 'uncipher'):
		out_file_name = file_source_name[:-5]

	out_file = open(out_file_name, 'wt')

	text = file_source.read()
	key  = file_key.read()

	num_text = [ord(c) for c in text]
	num_key  = [ord(c) for c in key]

	l = len(num_key)

	for (i, a) in enumerate(num_text, start = 0):
		b = num_key[i % l]
		c = chr(a ^ b)
		out_file.write(c)

	file_source.close()
	file_key.close()
	out_file.close()