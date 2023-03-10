import random

help_command_response = '```' \
                        'This is help message! \n' \
                        'List of available commands: \n' \
                        '- !help \n' \
                        '- !hello \n' \
                        '- !roll \n' \
                        '```'

hello_response = '> Hey there!'

roll_d6_command_response = f'> {str(random.randint(1, 6))}'

unknown_command_response = '> Unknown command. Try using "!help"'
