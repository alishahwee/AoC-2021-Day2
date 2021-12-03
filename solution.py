def part_one(commands: list[str]) -> int:
    horizontal_position = 0
    depth = 0

    for command in commands:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            horizontal_position += units
        elif direction == "down":
            depth += units
        elif direction == "up":
            depth -= units

    return horizontal_position * depth


def part_two(commands: list[str]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            horizontal_position += units
            depth += units * aim
        elif direction == "down":
            aim += units
        elif direction == "up":
            aim -= units

    return horizontal_position * depth
