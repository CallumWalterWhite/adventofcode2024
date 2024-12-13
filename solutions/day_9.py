from util.input import get_input_as_list

if __name__ == "__main__":
    input_data =     get_input_as_list("inputs/day_9.txt")[0][0]
    size = len(input_data)
    fs = []
    new_fs = []
    x = 0
    for i in range(size):
        if i % 2 == 0:
            fs.extend(int(input_data[i]) * [str(x)])
            x+=1
        else:
            fs.extend(int(input_data[i]) * ".")
    lp = 0
    rp = len(fs) - 1
    fs_c = fs.copy()
    while lp <= rp:
        if fs_c[lp] == ".":
            while lp < rp and fs_c[rp] == ".":
                rp -= 1
            if fs_c[rp] != ".":
                new_fs.append(int(fs_c[rp]))
            rp -= 1
        else:
            new_fs.append(int(fs_c[lp]))
        lp += 1
    print(sum([i * int(disk_id) for (i, disk_id) in enumerate(new_fs) if disk_id != '.'])) # part 1
    rp = len(fs_c) - 1
    fs_c = fs.copy()
    while 0 < rp:
        lp = 0
        if fs_c[rp] != ".":
            ch = fs_c[rp]
            lc = 0
            orp = rp
            while lp < rp and fs_c[rp] == ch:
                rp -= 1
                lc += 1
            while lp < rp and fs_c[lp:lp + lc] != ["."] * lc:
                lp += 1
            if fs_c[lp:lp + lc] == ["."] * lc:
                for i in range(lp, lp + lc):
                    fs_c[i] = ch
                for i in range(rp + 1, rp + lc + 1):
                    fs_c[i] = "."
        else:
            rp -= 1
    print(sum([i * int(disk_id) for (i, disk_id) in enumerate(fs_c) if disk_id != '.'])) # part 2