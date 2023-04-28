var img = document.getElementById("image-preview");

img.addEventListener("wheel", function (e) {
    e.preventDefault(); // 防止页面滚动
    var delta = e.deltaY || e.detail || e.wheelDelta;
    var zoom = delta > 0 ? 0.9 : 1.1; // 根据滚轮方向调整缩放比例
    img.style.width = img.offsetWidth * zoom + "px";
    img.style.height = img.offsetHeight * zoom + "px";
});


const selectElement = document.getElementById("algorithm");

selectElement.addEventListener("change", function () {
    const selectedOption = selectElement.value;
    ChangeAlgorithm(selectedOption);
});

const ChangeAlgorithm = async (selectedOption) => {
    // 发送 POST 请求
    const response = await fetch('/change', {
        method: 'POST',
        body: selectedOption
    });

    // 处理响应
    var div = document.getElementById('algorithm-settings');
    if (response.ok) {
        const data = await response.text();
        console.log('后端返回的数据: ', data);
        div.innerHTML = data;
    } else {
        console.error('请求失败: ', response.status);
    }
}


// 获取表单元素
const imageSettingsForm = document.getElementById('image-settings');
const tspAlgorithmSettingsForm = document.getElementById('TSP-Algorithm-settings');
const submitBtn = document.getElementById('submitBtn');

// 点击事件处理函数
const onSubmit = async () => {
    // 收集表单数据
    var input = document.querySelector('input[type="file"]');
    const formData = new FormData();
    for (const input of imageSettingsForm.elements) {
        if (input.name) formData.append(input.name, input.value);
    }
    for (const input of tspAlgorithmSettingsForm.elements) {
        if (input.name) formData.append(input.name, input.value);
    }
    formData.append('file', input.files[0]);

    document.getElementById('loader-wrapper').style.display = 'flex';
    // 发送 POST 请求
    const response = await fetch('/solve', {
        method: 'POST',
        body: formData
    });

    // 处理响应
    if (response.ok) {
        const data = await response.text();
        console.log('后端返回的数据: ', data);
        document.getElementById('image-preview').src = data;
        document.getElementById('loader-wrapper').style.display = 'none';
    } else {
        console.error('请求失败: ', response.status);
        document.getElementById('loader-wrapper').style.display = 'none';
    }
};

// 为按钮添加点击事件监听器
submitBtn.addEventListener('click', onSubmit);
