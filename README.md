# New Deep Dreams

This project aims to create Deep Dreams with modified methods, inspired by Tensorflow Lucid researches, and trying to implement generative solutions to make generating dreams less computationally demanding.

## Methodology

The authors aim to create new Deep Dreams with the following tools and architectures.

### Analizing existing style-transfer and Deep Dream methods

After some research we aim to recreate and study the existing usage of filter information. Our intention is to combine the best
of these methods to achieve greater performance and increase our knowledge.

### Retraining Imagenet trained networks

Using the pretrained low-level convolutional-layers as basic (but hopefully good) feature extractors, complex formations could be
learned by retraining the top levels of these networks. The team focuses on VGG, Inception networks.

### New methods

Using some tricks while doing gradient descent should result in various deep-dreams and representation extractions. Some of these might help us understand the organization and information handling of popular network architectures.

### Using generative methods

By training generative networks one should be able to use a smaller network to apply one specific deep dream filter to an image, thus making compact dream generators is one of our side-goals.

### ~~Audio~~

~~Our group planned to do some audio-styletransfers and dreams. Due to the fact that our project has a deadline and we have finite time, we're heading to a direction, which could involve more interesting ideas and solutions for now.~~

## Data

### Dataset 1 (Artificial)

This dataset contains images from 25 categories taken out from ImageNet. Having different types, shapes and colors our intention is that this dataset might be able to create a rich visual Deep Dream. 
Each category has at least 600 images but some of them has around 1000. Equalizing them might not be crucial in this usecase, therefore we haven't dropped any images yet. Preprocessing might differ depending on the used network, as a first approach we will resize every image to (244,244) size and normalize them. Some rotation or noise might be added later.
The list of these categories can be found here:
'altar','viaduct','Roman building','temple','totem pole','windmill','artillery, heavy weapon, gun, ordnance','launcher, rocket launcher','atom bomb, atomic bomb, A-bomb, fission bomb, plutonium bomb','shotgun shell','automatic firearm, automatic gun, automatic weapon','revolver, six-gun, six-shooter','khukuri','broad arrow','helicopter, chopper, whirlybird, eggbeater','biplane','stealth fighter','airbus','hot-air balloon','motor scooter, scooter','ambulance','sports car, sport car','Model T','jeep, landrover','stock car'

### Dataset 2 [Natural Images](https://www.kaggle.com/prasunroy/natural-images)

Natural images is a dataset of 8 categories 'airplane', 'cat', 'car', 'dog', 'flower', 'fruit', 'motorbike', 'person'. We wanted to have a relatively small dataset of not so large images (6899) to generate a specific kind of DeepDreams on them, we did so, thus we have Dataset 3.
This dataset used in **"Effects of Degradations on Deep Neural Network Architectures"** as a benchmark, the dataset was assembled by **Roy, Prasun and Ghosh, Subhankar and Bhattacharya, Saumik and Pal, Umapada**

### Dataset 3 (Natural Dreams)

This dataset was created from Dataset 2 with the following parameters of DeepDream generation:
-Model: InceptionV3, imagenet weights
-Image resize: 299x299
-Maplist (guide activations): None
-Number of recursion: 2
-Rescale factor: 0.85
-Blend: 0.15
-Iterations per recursion: [100,100,100]
-Step size: 0.02

Some sample images are provided, we will use this dataset to create and test generative models.


## Milestones

- [x] Style transfer with VGG    **Files: VGG19deepstyle.ipynb**
- [x] Standard Deep Dreams with VGG  **Files: dreamerVGG.ipynb**
- [x] Standard Deep Dreams with Inception   **Files: dreamerInception.ipynb**
- [ ] Standard Deep Dreams with GANs
- [x] Hacking with good ideas (Octaves, better resolution)
- [x] Setting up datasets   **Files: Sounds.ipynb, Dog_data_preprocess.ipynb, Dataset2_preproc.ipynb imnetdl.py, sound.pkl**
- [ ] ~~Retraining VGG to get new Dreams~~
- [x] Retraining Inception to get new Dreams
- [ ] Training GANs/AEs/Smaller CNNs to generate new Dreams -- In progress -- **Files: GANDream , t81_558_class_07_2_Keras_gan.ipynb**
- [ ] ~~Training own CNN architectures to get new Dreams~~
- [ ] ~~Training own CNN architectures to get audio style-transfer~~
- [ ] ~~Training own CNN architectures to get audio Dreams~~
- [ ] ~~Generating 2in1 Audio-visual dreams~~
- [x] Advanced dreams with guide images
- [ ] Using multiple guide images
- [ ] Exploring even more complex loss definitions
- [ ] Cleaning up code, packing it all together (Done for Stage 2)
- [ ] Final documentation


## Results

### GAN

The most popular field where we can use GANs is 'face-creation'. You can find lot of example and tutorial for generated random faces. In this project the generator learn the relevant points on face images. We give for this network deep dream images for training. It has big potential, but the first attempt it learnt the main object of the image and just a little bit of the dream. The second problem is GAN-s not too good with big images, to solve these problems would be a good task for the next few weeks.
<!--
## Authors
* **Name1** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name2** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name3** - *Worked on.....* - [gitname](https://github.com/gitname)
!-->
