import os
from PIL import Image
import numpy as np

def calculate_epsilon(img_path1, img_path2):
    # 加載並轉換圖片
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    if img1.size != img2.size:
        return False, "Image sizes are different.", 0

    img1_array = np.array(img1).astype(float)
    img2_array = np.array(img2).astype(float)
    
    # 計算最大差異
    diff = np.abs(img1_array - img2_array)
    max_diff = np.max(diff)  # 不標準化，直接使用像素差值

    epsilon_threshold = 8  # 直接使用像素值的差異
    is_below_epsilon = max_diff <= epsilon_threshold
    return is_below_epsilon, max_diff

def compare_folders_epsilon(folder1, folder2,ok):
    comparison_results = {}

    # 確保每個文件僅比較一次
    for file in files1:
        img1_path = os.path.join(folder1, file)
        img2_path = os.path.join(folder2, file)
        
        if os.path.isfile(img1_path) and os.path.isfile(img2_path):
            is_below_epsilon, max_diff = calculate_epsilon(img1_path, img2_path)
            if is_below_epsilon:
                ok+=1
            comparison_results[file] = (is_below_epsilon, max_diff)
        else:
            comparison_results[file] = (False, "Matching file not found or one is not a file.", 0)
    
    return comparison_results,ok

# 設定資料夾路徑
original_folder = '/home/adl/Desktop/zenn/SPML/SPML_HW1/cifar-100_eval'
adversarial_folder = '/home/adl/Desktop/zenn/SPML/SPML_HW1/result/adv_imgs'
files1 = os.listdir(original_folder)
files1.sort()  

ok = 0
# 執行比較
results,ok = compare_folders_epsilon(original_folder, adversarial_folder,ok)

# 輸出結果
for img_name, (is_below_epsilon, max_diff) in results.items():
    print(f"{img_name}: Epsilon <= 8: {is_below_epsilon}, Maximum Difference: {max_diff}")

print(ok,"/500 checked")