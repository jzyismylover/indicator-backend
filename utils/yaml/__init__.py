from yaml import safe_load
import os


def parseYAML(lines: list, n=0, index=0, s=dict()):
    """解析yaml文件"""
    dic = dict()
    while index < len(lines):
        if s.get(index) is not None:
            index = index + 1
            continue

        line = lines[index]
        if line == '':
            continue
        line = str(line)
        key, value = line.split(':')
        key = key.strip()
        value = value.strip().replace('\n', '')
        if line.startswith(' ' * n):
            if value is not '':
                dic[key] = value
            else:
                dic[key] = parseYAML(lines, n + 2, index + 1, s)
            s[index] = index
        elif line.startswith(' ' * (n - 2)):
            return dic

        index = index + 1

    print(s)
    return dic


if __name__ == '__main__':

    FILE_NAME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.yml'))
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        try:
            y = parseYAML(f.readlines())
            print(y)
            s = dict()
        except Exception as e:
            print(e)
            pass
