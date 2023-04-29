import tsplib95
import matplotlib.pyplot as plt
import math


def getPathLength(x_list: list, y_list: list) -> float:
    ret = 0
    for i in range(0, len(x_list)):
        ret += math.sqrt((x_list[i]-x_list[i-1])*(x_list[i]-x_list[i-1]) +
                         (y_list[i] - y_list[i-1])*(y_list[i] - y_list[i-1]))

    return ret


def GenerateImage(problem, tour: list, imagePath="../static/tmp.svg"):
    # 获取所有节点的坐标
    node_coords = problem.node_coords.items()
    sorted_nodes = sorted(node_coords, key=lambda x: tour.index(x[0]))

    x_list = [coord[0] for node_id, coord in sorted_nodes]
    y_list = [coord[1] for node_id, coord in sorted_nodes]

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis("off")

    plt.title(f"path length : {getPathLength(x_list,y_list)}")
    plt.plot(x_list, y_list, linewidth=1, color='black')
    plt.savefig(imagePath, format='svg')
