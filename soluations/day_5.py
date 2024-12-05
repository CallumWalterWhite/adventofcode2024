from util.input import get_input_as_string

# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47

if __name__ == "__main__":
    input_data = get_input_as_string("inputs/day_5.txt")
    g_nodes = []
    reports: list[str] = []
    for line in input_data.split("\n"):
        if "|" in line:
            g_nodes.append(list(map(int, line.split("|"))))
        elif "," in line:
            reports.append(list(map(int, line.split(","))))
    nodes = {}
    for node in g_nodes:
        if node[0] not in nodes:
            nodes[node[0]] = []
        if node[1] not in nodes:
            nodes[node[1]] = []
        nodes[node[0]].append(node[1])
    valid_reports = []
    invalid_reports = []
    total = 0
    for report in reports:
        pages = report.copy()
        pages.reverse()
        valid = True
        for i in range(len(pages) - 1):
            if pages[i + 1] in nodes[pages[i]]:
                valid = False
                break
        if valid:
            middle_page = len(report) // 2
            total += report[middle_page]
        else:
            invalid_reports.append(report)
    print(total)
    total = 0
    newvalid_reports = []
    for report in invalid_reports:
        pages = report.copy()
        pages.reverse()
        valid = False
        while not valid:
            inner_validtion = True
            for i in range(len(pages) - 1):
                if pages[i + 1] in nodes[pages[i]]:
                    node_v = pages[i]
                    pages.pop(i)
                    pages = pages[:i+1] + [node_v] + pages[i+1:]
                    inner_validtion = False
                    break
            if inner_validtion:
                valid = True
                middle_page = len(report) // 2
                total += report[middle_page]
            else:
                continue