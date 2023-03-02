# Function should return a dictionary/Object/Hash with "status" as a key, whose value can :
# "busy" or "available" depending on the truth value of the argument is_busy.

# But as you will see after clicking RUN or ATTEMPT this code has several bugs, please fix them


# Using "not" so it will work even if busy is different from 0 and 1
def get_status(is_busy):
    return {"status": ("busy", "available")[not is_busy]}
