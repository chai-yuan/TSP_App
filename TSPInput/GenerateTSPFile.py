import tqdm
from .voronoi import centroids
import imageio
import numpy as np


def normalize(D):
    Vmin, Vmax = D.min(), D.max()
    if Vmax - Vmin > 1e-5:
        D = (D-Vmin)/(Vmax-Vmin)
    else:
        D = np.zeros_like(D)
    return D


def initialization(n, D):
    """
    Return n points distributed over [xmin, xmax] x [ymin, ymax]
    according to (normalized) density distribution.

    with xmin, xmax = 0, density.shape[1]
         ymin, ymax = 0, density.shape[0]

    The algorithm here is a simple rejection sampling.
    """

    samples = []
    while len(samples) < n:
        X = np.random.uniform(0, D.shape[1], 10*n)
        Y = np.random.uniform(0, D.shape[0], 10*n)
        P = np.random.uniform(0, 1, 10*n)
        index = 0
        while index < len(X) and len(samples) < n:
            x, y = X[index], Y[index]
            x_, y_ = int(np.floor(x)), int(np.floor(y))
            if P[index] < D[y_, x_]:
                samples.append([x, y])
            index += 1
    return np.array(samples)


def GenerateTSPFile(imagePath: str, tspFilePath: str, point_num: int = 1024, iter_num: int = 15, threshold: int = 255):
    density = imageio.imread(imagePath, mode='L')
    # 我们希望每个voronoi区域（大约）有500个像素
    # 按图像尺寸划分像素数点
    zoom = (point_num * 500) / (density.shape[0]*density.shape[1])
    zoom = int(round(np.sqrt(zoom)))
    # density = scipy.ndimage.zoom(density, zoom, order=0) # 这是根据最后两行中的计算调整图像大小的位。
    # 将阈值应用于图像
    # 任何颜色>阈值都将为白色
    # 获得用于对照阈值进行检查的最小值
    density = np.minimum(density, threshold)

    density = 1.0 - normalize(density)
    # 将图像倒置？（为什么？可能是因为图像坐标轴颠倒了）
    density = density[::-1, :]
    density_P = density.cumsum(axis=1)
    density_Q = density_P.cumsum(axis=1)

    points = initialization(point_num, density)
    print("Number of points:", point_num)
    print("Number of iterations:", iter_num)

    xmin, xmax = 0, density.shape[1]
    ymin, ymax = 0, density.shape[0]
    bbox = np.array([xmin, xmax, ymin, ymax])
    ratio = (xmax-xmin)/(ymax-ymin)

    for i in tqdm.trange(iter_num):
        regions, points = centroids(
            points, density, density_P, density_Q)

    # Save stipple points and tippled image
    tspfileheader = "NAME : " + imagePath + "\nTYPE : TSP\nCOMMENT: Stipple of " + imagePath + " with " + \
        str(len(points)) + " points\nDIMENSION: " + str(len(points)
                                                        ) + "\nEDGE_WEIGHT_TYPE: ATT\nNODE_COORD_SECTION"
    nodeindexes = np.arange(1, len(points)+1)[:, np.newaxis]
    np.savetxt(tspFilePath, np.concatenate((nodeindexes, points), axis=1), [
        '%d', '%d', '%d'], header=tspfileheader, comments='')
