# Este es un ejemplo de instruccion condicional 
# if true_or_not:
#     do_this_if_true

# Usando un ejemplo de la vida real podemos verlo de la siguiente manera
# if the_weather_is_good:
#     go_for_a_walk()
# have_lunch()
# Sin importar de la condicion del clima, almorzar sigue siendo un hecho

# if sheep_counter >= 120: # Evaluate a test expression
#     sleep_and_dream() # Execute if test expression is True

hambre = True
if hambre is True:
    print("A que hora comemos?")

if hambre is False:
    print("No quiero gracias ")

# Cuando queremos realizar una instruccion incluso si no se cumplen los parametros
# del if implementamos el if-else

# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

# if the_weather_is_good:
#     go_for_a_walk()
#     have_fun()
# else:
#     go_to_a_theater()
#     enjoy_the_movie()
# have_lunch()

hambre = False
if hambre is True:
    print("Tengo Hambre")
else:
    print("No tengo hambre")

# Se puede hacer uso de un if dentro de un if para condicionar ciertas acciones
# Dentro de la misma condicion un ejemplo de esto seria 

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

hambre = True
antojo = True 
if hambre is True:
    print("Tienes ganas de algo en especifico?")
    if antojo is True:
        print("De que tienes antojo?")
else:
    print("Vamos mejor al cine")
# Existe otra conficional diferente el elif esto es un acronimo de else if
# Este se usa para checar mas de una condicion y detenerse cuando el primer
# hecho verdadero sea encontrado

# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

hambre = False
aburrido = True

if hambre is True:
    print("Vamos a comer")
elif aburrido is False:
    print("Quedemonos en casa")
elif aburrido is True:
    print("Vamos al cine")
