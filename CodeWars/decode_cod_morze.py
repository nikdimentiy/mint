def decodeMorse(morse_code):
    message = "".join(
        [morse_code[i] if i in morse_code else " " for i in morse_code.split(" ")])
    return message.replace("  ", " ").strip()
