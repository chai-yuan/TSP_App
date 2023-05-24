import os
import time
import tsplib95
from TSPInput import GenerateTSPFile
from TSPOutput.GenerateImage import GenerateImage
from TSPAlgorithm import TSP_Solver

input_images = ["./static/mascot.jpeg",
                "./static/scenery1.jpeg",
                "./static/scenery2.jpeg",
                "./static/scenery3.jpeg",
                "./static/scenery4.jpeg",
                "./static/scenery5.jpeg",
                "./static/scenery6.jpeg",
                "./static/scenery7.jpeg",
                "./static/scenery8.jpeg"]

prefix_path = "./tmp/NearestNeighborSolver"

if __name__ == "__main__":
    # 获取表单数据
    point_num = 20000
    iterative_times = 20
    threshold = 95
    # 执行算法流程
    tsp_file = os.path.join(prefix_path, "stipple.tsp")

    for input_image in input_images:
        print(f"file: {input_image}", 20*"-")
        output_filename = time.strftime(
            '%m_%d_%H_%M_%S', time.localtime()) + ".svg"
        output_image = os.path.join(prefix_path, output_filename)
        GenerateTSPFile(input_image, tsp_file, point_num=point_num,
                        iter_num=iterative_times, threshold=threshold)

        problem = tsplib95.load(tsp_file)
        tour = TSP_Solver["NearestNeighborSolver"].solve(
            problem, {})
        GenerateImage(problem=problem, tour=tour, imagePath=output_image)
