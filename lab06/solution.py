def count_by_extension(paths):
    counts = {}
    for path in paths:
        dot_position = path.rfind('.')
        if dot_position == -1:
            extension = ''
        else:
            extension = path[dot_position + 1:].lower()
        if extension in counts:
            counts[extension] += 1
        else:
            counts[extension] = 1
    return counts