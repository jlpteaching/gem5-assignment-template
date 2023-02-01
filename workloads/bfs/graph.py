import argparse


def get_inputs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("graph_name", type=str)
    args = argparser.parse_args()
    return args.graph_name


if __name__ == "__main__":
    graph_name = get_inputs()
    columns = []
    edges = []
    with open(graph_name, "r") as graph:
        prev_src = -1
        prefix_sum = 0
        max_dst = -1
        for line in graph.readlines():
            src = int(line.split()[0])
            dst = int(line.split()[1])
            if dst > max_dst:
                max_dst = dst
            if src != prev_src:
                for _ in range(src - prev_src):
                    columns.append(prefix_sum)
                prev_src = src
            edges.append(dst)
            prefix_sum += 1
        for _ in range(max_dst - prev_src):
            columns.append(prefix_sum)
    columns.append(len(edges))

    lines = [f"int columns [{len(columns)}] = {{ \n"]

    line = ""
    for column in columns:
        if line == "":
            line = f"{column}"
        else:
            line += f", {column}"
        if len(line) > 80:
            line += ", \n"
            lines.append(line)
            line = ""
    if line != "":
        line += " \n"
        lines.append(line)
    lines.append("}; \n")
    lines.append("\n")

    lines.append(f"int edges [{len(edges)}] = {{ \n")
    line = ""
    for edge in edges:
        if line == "":
            line = f"{edge}"
        else:
            line += f", {edge}"
        if len(line) > 80:
            line += ", \n"
            lines.append(line)
            line = ""
    if line != "":
        line += " \n"
        lines.append(line)
    lines.append("}; \n")
    lines.append("\n")
    lines.append("#endif // __BFS_GRAPH_H__\n")

    lines = [
        "#ifndef __BFS_GRAPH_H__\n",
        "#define __BFS__GRAPH_H__\n",
        "\n",
        f"int visited [{len(columns) - 1}] = {{0}};\n",
        "\n",
    ] + lines

    with open("graph.h", "w") as header_file:
        header_file.writelines(lines)
