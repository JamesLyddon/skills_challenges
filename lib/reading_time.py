def reading_time(text):
    if text is None:
        raise Exception("please provide a passage")
    reading_speed = 200
    return text / reading_speed