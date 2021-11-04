#codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
def snail(snail_map):
    result = []
    while len(snail_map) > 1:
        result.append(snail_map[0])
        snail_map = snail_map[1:]
        result.append([i[-1] for i in snail_map])
        snail_map = [i[:-1] for i in snail_map]
        result.append(snail_map[-1][::-1])
        snail_map = snail_map[:-1]
        result.append([i[0] for i in snail_map[::-1]])
        snail_map = [i[1:] for i in snail_map]
    return [j for i in result for j in i] + [[] if not snail_map else snail_map[0]][0]
