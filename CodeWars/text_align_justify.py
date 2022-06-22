def justify(text, width):

    if text == '':
        return ''
    words = text.split()
    justified = ''
    line = words[0]
    words.remove(line)
    for word in words:
        if len(line)+len(word)+1 <= width:
            line = line + ' '
            line = line + word
        else:
            spaces_needed_total = width - len(line)
            spaces_in_line = line.count(' ')
            if spaces_in_line != 0:
                all_spaces_lenght, add_at_begining = divmod(
                    spaces_needed_total, spaces_in_line)
                line = line.replace(
                    ' ', ' '*(all_spaces_lenght+2), add_at_begining)
                line = (' '*(all_spaces_lenght+1)
                        ).join(line.rsplit(" ", spaces_in_line-add_at_begining))

            justified = justified + line
            justified = justified + '\n'
            line = word
    justified = justified + line
    return justified
