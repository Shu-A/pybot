import re

def script(robot):
    pattern = robot.name + '\\?$'
    flags = re.I
    name_regex = re.compile(pattern, flags)

    rep_msg = "What's going on ?"
    robot.hear(name_regex, lambda(msg): msg.reply(msg.random, rep_msg))
