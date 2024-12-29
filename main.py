import game_interface

print("=== WA-TOR SIMULATION ===")
while True:
    s = input("Select interface (C: command line, G: graphical): ").lower()
    if (s == 'c'):
        itf = game_interface.CommandInterface()
        break
    elif (s == 'g'):
        itf = game_interface.GraphicalInterface()
        break
    else:
        print("Invalid input")

itf.run()
