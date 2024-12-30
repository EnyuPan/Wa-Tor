import game_interface

print("=== WA-TOR SIMULATION ===")
while True:
    s = input("Select interface (C: command line, G: graphical): ").strip().lower()
    if (s == 'c'):
        itf = game_interface.CommandInterface()
        break
    elif (s == 'g'):
        itf = game_interface.GraphicalInterface()
        break
    elif (s == 'q'):
        exit()
    else:
        print("Interface not recognized. Please try again.")

itf.run()
