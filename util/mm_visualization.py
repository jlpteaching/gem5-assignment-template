import os
import imageio
import numpy as np
import matplotlib.pyplot as plt


class VizParams:
    def __init__(self, A, B, C, padding=0.5, scale=1, outdir="animate"):
        self.a_h, self.a_w = np.shape(A)
        self.b_h, self.b_w = np.shape(B)
        assert self.a_w == self.b_h
        self.c_h = self.a_h
        self.c_w = self.b_w
        assert self.c_h, self.c_w == np.shape(C)
        self.t_h, self.t_w = self.b_h, self.a_w

        self.padding = padding
        self.scale = scale
        self.outdir = outdir

        self.total_cols = self.a_w + self.c_w + self.padding
        self.total_rows = self.b_h + self.c_h + self.padding
        self.fig_width = self.total_cols * scale
        self.fig_height = self.total_rows * scale

        self.a_x_offset = 0
        self.a_y_offset = 0
        self.b_x_offset = self.a_w + self.padding
        self.b_y_offset = self.c_h + self.padding
        self.c_x_offset = self.a_w + self.padding
        self.c_y_offset = 0
        self.t_x_offset = 0
        self.t_y_offset = self.a_h + self.padding

        self.a_rect = (
            (self.a_x_offset / self.total_cols),
            (self.a_y_offset / self.total_rows),
            (self.a_w / self.total_cols),
            (self.a_h / self.total_rows),
        )
        self.b_rect = (
            (self.b_x_offset / self.total_cols),
            (self.b_y_offset / self.total_rows),
            (self.b_w / self.total_cols),
            (self.b_h / self.total_rows),
        )
        self.c_rect = (
            (self.c_x_offset / self.total_cols),
            (self.c_y_offset / self.total_rows),
            (self.c_w / self.total_cols),
            (self.c_h / self.total_rows),
        )
        self.t_rect = (
            (self.t_x_offset / self.total_cols),
            (self.t_y_offset / self.total_rows),
            (self.t_w / self.total_cols),
            (self.t_h / self.total_rows),
        )
        if os.path.isabs(self.outdir):
            output_path = self.outdir
            output_path = os.path.join(os.getcwd(), self.outdir)
            if not os.path.exists(output_path):
                print(f"{output_path} does not already exist.")
                os.mkdir(output_path)
                print(f"Created {output_path}")
            else:
                print(f"{output_path} already exists.")
                print(f"Deleting everything in {output_path}")
                for delete in os.scandir(output_path):
                    os.remove(delete.path)
            print(
                f"{output_path} is ready to be filled with animation frames."
            )
        else:
            output_path = os.path.join(os.getcwd(), self.outdir)
            if not os.path.exists(output_path):
                print(f"{output_path} does not already exist.")
                os.mkdir(output_path)
                print(f"Created {output_path}")
            else:
                print(f"{output_path} already exists.")
                print(f"Deleting everything in {output_path}")
                for delete in os.scandir(output_path):
                    os.remove(delete.path)
            print(
                f"{output_path} is ready to be filled with animation frames."
            )
            self.outdir = output_path


class VisAxes:
    def __init__(self, a_ax, b_ax, c_ax, t_ax):
        self.a_ax = a_ax
        self.b_ax = b_ax
        self.c_ax = c_ax
        self.t_ax = t_ax


def make_axes(fig, vis_params):
    a_ax = fig.add_axes(vis_params.a_rect)
    a_ax.set_yticks([(y - 0.5) for y in range(vis_params.a_h)])
    a_ax.set_xticks([(x - 0.5) for x in range(vis_params.a_w)])
    a_ax.set_yticklabels([])
    a_ax.set_xticklabels([])
    a_ax.grid()

    b_ax = fig.add_axes(vis_params.b_rect)
    b_ax.set_yticks([(y - 0.5) for y in range(vis_params.b_h)])
    b_ax.set_xticks([(x - 0.5) for x in range(vis_params.b_w)])
    b_ax.set_yticklabels([])
    b_ax.set_xticklabels([])
    b_ax.grid()

    c_ax = fig.add_axes(vis_params.c_rect)
    c_ax.set_yticks([(y - 0.5) for y in range(vis_params.c_h)])
    c_ax.set_xticks([(x - 0.5) for x in range(vis_params.c_w)])
    c_ax.set_yticklabels([])
    c_ax.set_xticklabels([])
    c_ax.grid()

    t_ax = fig.add_axes(vis_params.t_rect)
    t_ax.set_xticklabels([])
    t_ax.axis("off")

    return VisAxes(a_ax, b_ax, c_ax, t_ax)


def print_highlight(
    vis_params, vis_axes, a_coord=None, b_coord=None, c_coord=None
):
    a_bg = np.zeros((vis_params.a_h, vis_params.a_w))
    if not a_coord is None:
        a_bg[a_coord[0], a_coord[1]] = 1
    vis_axes.a_ax.imshow(a_bg)

    b_bg = np.zeros((vis_params.b_h, vis_params.b_w))
    if not b_coord is None:
        b_bg[b_coord[0], b_coord[1]] = 1
    vis_axes.b_ax.imshow(b_bg)

    c_bg = np.zeros((vis_params.c_h, vis_params.c_w))
    if not c_coord is None:
        c_bg[c_coord[0], c_coord[1]] = 1
    vis_axes.c_ax.imshow(c_bg)


def print_matrices(A, B, C, vis_params, vis_axes):
    for row in range(vis_params.a_h):
        for col in range(vis_params.a_w):
            vis_axes.a_ax.annotate(
                A[row][col],
                xy=(col, row),
                fontsize=12,
                color="red",
                xycoords="data",
            )

    for row in range(vis_params.b_h):
        for col in range(vis_params.b_w):
            vis_axes.b_ax.annotate(
                B[row][col],
                xy=(col, row),
                fontsize=12,
                color="red",
                xycoords="data",
            )

    for row in range(vis_params.c_h):
        for col in range(vis_params.c_w):
            vis_axes.c_ax.annotate(
                C[row][col],
                xy=(col, row),
                fontsize=12,
                color="red",
                xycoords="data",
            )


def print_madd_operation(A, B, C, i, j, k, vis_params, vis_axes):
    vis_axes.t_ax.annotate(
        f"C[{i}][{j}] = C[{i}][{j}] + A[{i}][{k}] * B[{k}][{j}]",
        xy=(0, 0.6),
        fontsize=12,
        color="blue",
        fontweight="bold",
        xycoords="data",
    )
    vis_axes.t_ax.annotate(
        f"C[{i}][{j}] = {C[i, j]} + {A[i, k]} * {B[k, j]}",
        xy=(0, 0.4),
        fontsize=12,
        color="blue",
        fontweight="bold",
        xycoords="data",
    )


def print_wb_result(A, B, C, i, j, k, vis_params, vis_axes):
    vis_axes.t_ax.annotate(
        f"C[{i}][{j}] = {C[i, j] + A[i, k] * B[k, j]}",
        xy=(0, 0.5),
        fontsize=12,
        color="blue",
        fontweight="bold",
        xycoords="data",
    )


def multiply_and_create_frames(A, B, C, i, j, k, frame_number, vis_params):
    fig = plt.figure()
    fig.set_size_inches(vis_params.fig_width, vis_params.fig_height)
    vis_axes = make_axes(fig, vis_params)
    print_highlight(vis_params, vis_axes)
    print_matrices(A, B, C, vis_params, vis_axes)
    fig.savefig(f"{vis_params.outdir}/{frame_number}.png")
    plt.close()
    frame_number += 1

    fig = plt.figure()
    fig.set_size_inches(vis_params.fig_width, vis_params.fig_height)
    vis_axes = make_axes(fig, vis_params)
    print_highlight(
        vis_params, vis_axes, a_coord=(i, k), b_coord=(k, j), c_coord=(i, j)
    )
    print_matrices(A, B, C, vis_params, vis_axes)
    fig.savefig(f"{vis_params.outdir}/{frame_number}.png")
    plt.close()
    frame_number += 1

    fig = plt.figure()
    fig.set_size_inches(vis_params.fig_width, vis_params.fig_height)
    vis_axes = make_axes(fig, vis_params)
    print_highlight(
        vis_params, vis_axes, a_coord=(i, k), b_coord=(k, j), c_coord=(i, j)
    )
    print_matrices(A, B, C, vis_params, vis_axes)
    print_madd_operation(A, B, C, i, j, k, vis_params, vis_axes)
    fig.savefig(f"{vis_params.outdir}/{frame_number}.png")
    plt.close()
    frame_number += 1

    fig = plt.figure()
    fig.set_size_inches(vis_params.fig_width, vis_params.fig_height)
    vis_axes = make_axes(fig, vis_params)
    print_highlight(vis_params, vis_axes, c_coord=(i, j))
    print_matrices(A, B, C, vis_params, vis_axes)
    print_wb_result(A, B, C, i, j, k, vis_params, vis_axes)
    fig.savefig(f"{vis_params.outdir}/{frame_number}.png")
    plt.close()
    frame_number += 1

    C[i][j] += A[i][k] * B[k][j]

    fig = plt.figure()
    fig.set_size_inches(vis_params.fig_width, vis_params.fig_height)
    vis_axes = make_axes(fig, vis_params)
    print_highlight(vis_params, vis_axes, c_coord=(i, j))
    print_matrices(A, B, C, vis_params, vis_axes)
    fig.savefig(f"{vis_params.outdir}/{frame_number}.png")
    plt.close()
    frame_number += 1

    return frame_number


def create_gif_from_frames(frames_dir, frame_number):
    images = []
    for i in range(frame_number):
        images.append(imageio.imread(f"{frames_dir}/{i}.png"))
    imageio.mimsave(f"{frames_dir}/animation.gif", images, duration=0.5)
