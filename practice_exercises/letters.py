def main():
   names = ["Mario", "Luigi", "Daisy", "Yoshi"]
   for name in names:
       print(write_letter (names, "Pricess Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to ball at 
    Peach's Castle this evening, 7:00PM.

    Sincerely,
    {sender}

    """

main()