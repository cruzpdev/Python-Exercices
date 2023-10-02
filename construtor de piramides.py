def build_pyramid(n):
    tower = []
    for floor in range(1, n + 1):
        spaces = " " * (n - floor)  # Padding spaces on the left
        blocks = "*" * (2 * floor - 1)  # Asterisks for the tower blocks
        row = spaces + blocks + spaces  # Combine spaces and blocks
        tower.append(row)
    return tower