from screeninfo import get_monitors

for m in get_monitors():        # every monitors
    print(m)                    # monotor object
    print(m.width, m.height)    # width, height

monitor = get_monitors()[0]
print("Monitor Width: {}, Monitor Height: {}".format(
    monitor.width, monitor.height))


def get_screen_size():

    from screeninfo import get_monitors

    monitor = get_monitors()[0]
    print(monitor)

    SCREEN_WIDTH = monitor.width
    SCREEN_HEIGHT = monitor.height
