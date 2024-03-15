# Adversarial Attack on Cifar-100
## Data Set
* Cifar-100 : https://www.cs.toronto.edu/~kriz/cifar.html
* cifar-100_eval : 500 images from Cifar-100 training set (5 images of each class).
## Attack strategies
* torchattack : https://github.com/Harry24k/adversarial-attacks-pytorch?tab=readme-ov-file
## Adversarail Examples
### Apple --> Sunflower
<img src = "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/imagePares/0_2.png" width="600" height="300">

### Fox --> Leopard
<img src = "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/imagePares/34_4.png" width="600" height="300">

### Snail --> Plate
<img src = "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/imagePares/77_4.png" width="600" height="300">

## Results
### FGSM
<img src= "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/AccVsEps/Accuracy_of_Source_Models_on_Target_Models_using_FGSM_Attack.png" width="800" height="600">

### PGD
<img src= "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/AccVsEps/Accuracy_of_Source_Models_on_Target_Models_using_PGD_Attack.png" width="800" height="600">

### Combined
<img src= "https://github.com/zenn19991231/Adversarial_attacks_on_Cifar-100/blob/main/result/AccVsEps/Accuracy_of_Source_Models_on_Target_Models_using_Combine_Attack.png" width="800" height="600">

## Run the code
``src/adversarial_attack.ipynb``
