# Santa is coming to town and he needs your help finding out who's been naughty or nice.
# You will be given an entire year of JSON data following this format:

# An example

# {
#     January: {
#         '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
#     },
#     February: {
#         '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
#     },
#     ...
#     December: {
#         '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
#     }
# }
# Your function should return "Naughty!" or "Nice!" depending on the total number
# of occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"

def naughty_or_nice(data):
    counter = {"Naughty": 0, "Nice": 0}
    for m in data:
        for k in data[m]:
            if data[m][k] == "Naughty":
                counter["Naughty"] += 1
            else:
                counter["Nice"] += 1
    return "Naughty!" if counter["Naughty"] > counter["Nice"] else "Nice!"
