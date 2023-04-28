from flask import Flask, render_template, request, jsonify
import os
import time
import tsplib95
from TSPInput import GenerateTSPFile
from TSPOutput.GenerateImage import GenerateImage
from TSPAlgorithm import TSP_Solver

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', image_url="/static/0.svg")


@app.route('/change', methods=['POST'])
def handle_change():
    # 如果算法选项发生改变，那么更新算法的配置单
    algorithm = str(request.data, encoding="utf8")
    return TSP_Solver[algorithm].setting()


@app.route('/solve', methods=['POST'])
def handle_solve():
    # 获取表单数据
    point_num = int(request.form.get('point_num'))
    iterative_times = int(request.form.get('iterative_times'))
    threshold = int(request.form.get('threshold'))
    algorithm = request.form.get('algorithm')
    # 保存上传图片
    file = request.files['file']
    input_image = os.path.join('./static/', file.filename)
    tsp_file = "./static/stipple.tsp"
    output_filename = time.strftime(
        '%m_%d_%H_%M_%S', time.localtime()) + ".svg"
    output_image = os.path.join('./static/', output_filename)
    file.save(input_image)
    # 执行算法流程
    GenerateTSPFile(input_image, tsp_file, point_num=point_num,
                    iter_num=iterative_times, threshold=threshold)
    problem = tsplib95.load(tsp_file)
    tour = TSP_Solver[algorithm].solve(problem, request.form.to_dict())
    GenerateImage(problem=problem, tour=tour, imagePath=output_image)

    return '/static/'+output_filename


if __name__ == '__main__':
    app.run(port=10086)
