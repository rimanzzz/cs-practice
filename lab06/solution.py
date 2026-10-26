
def count_by_extension(paths):
    counts = {}

    for path in paths:
        filename = path.rsplit('/', 1)[-1]
        dot_position = filename.rfind('.')

        if dot_position <= 0:
            extension = ''
        else:
            extension = filename[dot_position + 1:].lower()

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
    B = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    while n_bytes >= 1024:
        n_bytes /= 1024
        index += 1
    if index == 0:
        return f'{int(n_bytes)} {B[index]}'
    return f'{n_bytes:.1f} {B[index]}'