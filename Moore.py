import json # Mengimpor modul json untuk membaca file JSON

with open('Tugas 4 Otomata/input.json', 'r') as f: # Membuka file json yang berisi konfigurasi Moore Machine
	system = json.load(f) # Membaca dan memuat isi file JSON ke dalam variabel system
	states = system['states'] # Mengambil daftar state dan output dari system
	transitions = system['transitions'] # Mengambil fungsi transisi antar state berdasarkan input simbol 0 atau 1
	test = system['test_string'] # Menguji string apakah valid berdasarkan input
	curr_state = system['initial_state'] # State awal tempat machine mulai bekerja
	output = states[curr_state] # Output awal berdasarkan initial state 

	print(f'Path: {curr_state}', end='') # Mencetak path awal dari proses input yang dimulai dari initial state

	for val in test: # Memproses setiap simbol dalam test_string
		curr_state = transitions[curr_state][val] # Update current state berdasarkan input dan transisi
		output += states[curr_state] # Menambahkan output dari state baru ke dalam hasil output
		print(f' -> {curr_state}', end='') # Mencetak transisi ke state berikutnya
	
	print(f'\nOutput: {output}') # Mencetak hasil akhir output setelah semua input diproses