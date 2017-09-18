raining = input('Идет дождь?') #да или нет
temperature = int(input('Сколько градусов?')) # число

if temperature > 20 and not raining:
    print("Иди гуляй, что как сыч сидишь!")
elif temperature > 24:
    print("ну вообще и помокнуть можно так-то...")
else:
    print("Го в доту я создал")

