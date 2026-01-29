kardus = ['Mangga', 'Apel', 'Angga', 'Rafi', 'Jeruk']
start_from =  1
print(kardus[1 - start_from])
# print(*kardus)
# print(kardus[len(kardus) - 1])

tmp_kardus = kardus

print(f'kardus -> {kardus}')

tmp_kardus[1 - 1] = 'petrov'
print(f'tmp_kardus -> {tmp_kardus}')