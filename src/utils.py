def user_query_input():
        try:
            user_input = input("Ingresa tu consulta")
            if not user_input.isalpha():
                raise ValueError("Debe contener solo caracteres alfabéticos. Por favor, intenta de nuevo.")
            return user_input
        except ValueError as e:
            print(e)

def user_gpt_input():
        try:
            user_input = input("¿Quieres mejorar el texto?").strip().lower()
            if user_input not in ['yes', 'no']:
                raise ValueError("La respuesta debe ser 'yes' o 'no'. Por favor, intenta de nuevo.")
            return user_input == 'yes'
        except ValueError as e:
            print(e)

def user_translate_input():
        try:
            user_input = input("¿Quieres traducir el texto?").strip().lower()
            if user_input not in ['yes', 'no']:
                raise ValueError("La respuesta debe ser 'yes' o 'no'. Por favor, intenta de nuevo.")
            return user_input == 'yes'
        except ValueError as e:
            print(e)


print(user_query_input())
print(user_gpt_input())
print(user_translate_input())