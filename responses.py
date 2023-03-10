import string_responses


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message[0] == '!':
        if p_message[1:] == "hello":
            return string_responses.hello_response

        if p_message[1:] == 'roll d6':
            return string_responses.roll_d6_command_response

        if p_message[1:] == 'help':
            return string_responses.help_command_response

        return string_responses.unknown_command_response
