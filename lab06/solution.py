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


def deepest_path(paths):
    best_path = ''
    max_path = -1
    for path in paths:
        count_path = path.count('/')
        if count_path > max_path:
            max_path = count_path
            best_path = path
        if count_path == max_path and path < best_path:
            best_path = path
    return best_path


def human_size(n_bytes):
    index = 0
    B = ["B", "KB", "MB", "GB", "TB"]
    while n_bytes >= 1024:
        n_bytes /= 1024
        index += 1
    return f'{n_bytes:.1f}' + ' ' + B[index]