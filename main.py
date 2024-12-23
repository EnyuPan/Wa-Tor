from game_interface import CommandInterface

cli = CommandInterface()
while cli.game.running:
    if cli.game.active:
        cli.update_display()
    cli.handle_input()
