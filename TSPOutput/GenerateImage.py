import tsplib95
import matplotlib.pyplot as plt


def GenerateImage(problem, tour: list, imagePath="../static/tmp.svg"):
    # 获取所有节点的坐标
    node_coords = problem.node_coords.items()
    sorted_nodes = sorted(node_coords, key=lambda x: tour.index(x[0]))

    x_list = [coord[0] for node_id, coord in sorted_nodes]
    y_list = [coord[1] for node_id, coord in sorted_nodes]

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis("off")

    plt.plot(x_list, y_list, linewidth=1, color='black')
    plt.savefig(imagePath, format='svg')
