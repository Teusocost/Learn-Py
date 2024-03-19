idade = int(input("Digite a idade"))

print(idade)

if (idade <18):
    print("Menor de idade")
elif 18 <= idade <21:
    print("Maior de idade, pode votar mas não pode beber")
elif 21<=idade < 65:
    print("Maior de idade, pode votar e pode beber")
else:
    print("Idoso, pode beer mas n precisa votar")
    if idade > 90:
        print("E também é um ancião, parabens")