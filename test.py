import vomm
training_data = [ord(x) - 97 for x in "abababab" ]

my_model  = vomm.ppm()
my_model.fit(training_data, d=2, alphabet_size=2)
data = my_model.generate_data(length=300)
print(''.join([chr(x+97) for x in data]))
print(my_model)