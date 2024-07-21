API_KEY = 'gAAAAABmnW4wr-LKMcfKtgQWveuAAtWPeNESNacYCjOJRMpV49cEhKdPyXiDP3yJOuJTcuA8Qy8HsFjM3OQJamYlfMcL_ncuMgwxThidUjB_UbsUtPKxluurAFNIwQNifopU0beCi_Q4'

def get_user_input(prompt):
    return input(prompt).strip()

def get_user_confirmation(action):
    response = input(f"¿Quieres {action}? (s/n): ").strip().lower()
    return response == 's'

