def rgb(r, g, b):
    r, g, b = map(lambda x: 0 if x < 0 else 255 if x > 255 else x, [r, g, b])

    return "%s%s%s" % (format(r, "02X"), format(g, "02X"), format(b, "02X"))
