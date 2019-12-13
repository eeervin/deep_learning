# New Deep Dreams

This project aims to create Deep Dreams with modified methods, inspired by Tensorflow Lucid researches, and trying to implement generative solutions to make generating dreams less computationally demanding.
The documentation of this project is Deeplearning_HW.pdf.

## Usage

- For Deep Dreaming run DeepDream.ipynb, use for this google collaboratory and before it upload resources to your google drive folder.
- For using GAN to Deep Dreaming run GANDream.ipynb, also use google colab and for a dreams folder put some deep dreamed image, the output images will be in a folder with output name.

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
- Model: InceptionV3, imagenet weights  
- Image resize: 299x299  
- Maplist (guide activations): None  
- Number of recursion: 2  
- Rescale factor: 0.85  
- Blend: 0.15  
- Iterations per recursion: [100,100,100]  
- Step size: 0.02  
  
Some sample images are provided [here](https://github.com/eeervin/deep_learning/tree/master/results/Dataset_NaturalDreams), we will use this dataset to create and test generative models.
![Sample](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Dataset_NaturalDreams/flower/flower_0012.jpg "Yes, that's a flower")

## Milestones

- [x] Style transfer with VGG    **Files: VGG19deepstyle.ipynb**
- [x] Standard Deep Dreams with VGG  **Files: dreamerVGG.ipynb**
- [x] Standard Deep Dreams with Inception   **Files: dreamerInception.ipynb**
- [ ] ~~Standard Deep Dreams with GANs~~
- [x] Hacking with good ideas (Octaves, better resolution) **Files: DeepDream.ipynb**
- [x] Setting up datasets   **Files: Sounds.ipynb, Dog_data_preprocess.ipynb, Dataset2_preproc.ipynb imnetdl.py, sound.pkl**
- [ ] ~~Retraining VGG to get new Dreams~~ (No usable results)
- [x] Retraining Inception to get new Dreams **Files: Retrain_InceptionV3.ipynb, dataset_artificial_retrained.hdf5**
- [x] Training GANs/AEs/Smaller CNNs to generate new Dreams **Files: GANDream.ipynb , t81_558_class_07_2_Keras_gan.ipynb**
- [ ] ~~Training own CNN architectures to get new Dreams~~ (No usable results)
- [ ] ~~Training own CNN architectures to get audio style-transfer~~ (Audio part of the project dropped)
- [ ] ~~Training own CNN architectures to get audio Dreams~~ (Audio part of the project dropped)
- [ ] ~~Generating 2in1 Audio-visual dreams~~
- [x] Advanced dreams with guide images **Files: DeepDream.ipynb**
- [ ] ~~Using multiple guide images~~
- [ ] ~~Exploring even more complex loss definitions~~
- [x] Cleaning up code, packing it all together
- [x] Final documentation


## Results


### GAN

The most popular field where we can use GANs is 'face-creation'. You can find lot of example and tutorial for generated random faces. In this project the generator learn the relevant points on face images. We give for this network deep dream images for training. It has big potential, but the first attempt it learnt the main object of the image and just a little bit of the dream. The second problem is GAN-s not too good with big images, to solve these problems would be a good task for the next few weeks.

### HD images

With some research made on popular DeepDream methods, we decided to do a "rescale and blend" type of optimization, with small tiles taken out of randomly rolled images to have input sizes we are able to handle and avoid having sharp stripes.  
We start with the lowest resolution (smallest) image, to draw the outline of largescale features, then proceed to higher resolutions.  
Here, we present some of the results made with different filter sets of mixed5 and mixed3 layers.

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/HD_dreams/result1.jpg "HD_image")

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/HD_dreams/result2_1.jpg "HD_image")

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/HD_dreams/result2_2.jpg "HD_image")


### Guided Dreams

As a crossover of DeepStyle and DeepDream, we created some Guided Dreams. In this case the gradient ascent is weighted with the previously acquired activations of a guide image (it could be a batch too, if needed). For the images presented bellow, we used a modified loss function, and used the normalized values of activations on each corresponding filter of the dream layers.

As a base image we used our University.
![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/bme.jpg "BME")

Adding some unguided dreams would look like this:

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/bme_unguided.png "BME_Unguided")

Then comes a guide image, for example these traditional ornaments:

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/matyo.jpg "Guide_matyo")

And using this as a guide image, but changing nothing else, our dream changes:

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/bme_matyo.png "BME_Matyo")

Surprisingly if more basic features are used, we need to choose lower level layers, to get a good representation.
When using a beehive, like the upcoming one, layers like merge5 activated filters belonging to bee-parts, or entire bugs, while the hexagonal holes were represented in lower layers, therefore we moved to merge2.

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/beehive.jpg "Guide_Beehive")

The result is pretty nice:

![HD_image](https://raw.githubusercontent.com/eeervin/deep_learning/master/results/Guided_dreams/beeme.png "BME_Bee")

Future work on this topic is needed, and we plan to use these weights locally not just on a filter level.


<!--
## Authors
* **Name1** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name2** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name3** - *Worked on.....* - [gitname](https://github.com/gitname)
!-->
