from game_interface import CommandInterface

print("=== WA-TOR SIMULATION ===")
while True:
    s = input("Select interface (C: command line, G: graphical): ").lower()
    if (s == 'c'):
        itf = CommandInterface()
        break
    elif (s == 'g'):
        print("Graphical interface not yet implemented")
    else:
        print("Invalid input")

while itf.game.running:
    if itf.game.active:
        itf.update_display()
    itf.handle_input()
