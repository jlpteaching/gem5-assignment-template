
import argparse
from numpy.random import randint

def get_inputs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("array_size", type=int)
    args = argparser.parse_args()
    return args.array_size

if __name__ == "__main__":
    array_size = get_inputs()

    array = randint(low=-100000000, high=1000000000, size=array_size)

    lines = ["int data [ARRAY_SIZE] = { \n"]
    line = ""
    for element in array:
        if line == "":
            line = f"{element}"
        else:
            line += f", {element}"
        if len(line) > 80:
            line += ", \n"
            lines.append(line)
            line = ""
    if line != "":
        line += " \n"
        lines.append(line)
    lines.append("}; \n")
    lines.append("\n")

    lines.append("#endif // __BUBBLE_ARRAY_H__\n")

    lines = ["#ifndef __BUBBLE_ARRAY_H__\n",
            "#define __BUBBLE_ARRAY_H__\n",
            "\n",
            f"#define ARRAY_SIZE {array_size}\n",
            "\n"
            ] + lines

    with open("array.h", "w") as header_file:
        header_file.writelines(lines)