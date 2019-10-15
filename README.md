# Multimodal Deep Dreams

This project aims to create Deep Dreams with correlating audio-visual filters while digging deeper the hidden behaviour of CNNs.

## Methodology

The authors aim to create new Deep Dreams with the following tools and architectures.

### Analizing existing style-transfer and Deep Dream methods

After some research we aim to recreate and study the existing usage of filter information. Our intention is to combine the best
of these methods to achieve greater performance and increase our knowledge.

### Retraining Imagenet trained networks

Using the pretrained low-level convolutional-layers as basic (but hopefully good) feature extractors, complex formations could be
learned by retraining the top levels of these networks. The team focuses on VGG, Inception networks.

### Using GANs

As a side-effect of latent-space analysis generative adversarial networks are able to provide various dreamlike filters which
could be applied to images to create new Deep Dreams.

### Audio

Audio style-transfers and Deep Dreams are not as popular as their visual siblings, therefore we would like to put some effort
into the topic and come up with basic Mel spectrum based solutions.

### Video

As the final product of our project we will use Deep Dream on video and audio channels of a short movie hopefully getting
visual and musical dreams at the same time.

## Data

Each teammember set up a smaller dataset with categories that go well together in style.

###Dataset1

This dataset contains images of popular dog species and various dog sounds, creating a perfectly matching theme for four-legged Deep Dreams.

###Dataset 2 (Artificial)

This dataset contains images from 25 categories taken out from ImageNet. Having different types, shapes and colors our intention is that this dataset might be able to create a rich visual Deep Dream. 
Each category has at least 600 images but some of them has around 1000. Equalizing them might not be crucial in this usecase, therefore we haven't dropped any images yet. Preprocessing might differ depending on the used network, as a first approach we will resize every image to (244,244) size and normalize them. Some rotation or noise might be added later.
The list of these categories can be found here:
'altar','viaduct','Roman building','temple','totem pole','windmill','artillery, heavy weapon, gun, ordnance','launcher, rocket launcher','atom bomb, atomic bomb, A-bomb, fission bomb, plutonium bomb','shotgun shell','automatic firearm, automatic gun, automatic weapon','revolver, six-gun, six-shooter','khukuri','broad arrow','helicopter, chopper, whirlybird, eggbeater','biplane','stealth fighter','airbus','hot-air balloon','motor scooter, scooter','ambulance','sports car, sport car','Model T','jeep, landrover','stock car'

Audio data is extracted from the FSDKaggle2018 dataset, from which we have chosen 20 categories. It contains around 5000 samples unequally distributed between the categories. As mentioned above no equalization happens here. Preprocessing invloves standardization and spectrum generation, on which we run our CNN networks.
The list of these categories can be found here:
"Acoustic_guitar", "Bus", "Chime", "Computer_keyboard","Cowbell", "Drawer_open_or_close", "Fireworks", "Glockenspiel", "Gong", "Gunshot_or_gunfire", "Keys_jangling", "Knock", "Microwave_oven","Scissors", "Shatter", "Snare_drum", "Squeak", "Tearing", "Telephone", "Writing"


###Dataset3 (Bird sounds)

This dataset contains sounds from birds. These were recognized very different environment so we hear different noises in these files. This dataset was the development data for the bird audio detection challenge on http://machine-listening.eecs.qmul.ac.uk site. It contains about 8000 wav files. For the testing the first 100 row stored in pkl file, so it can be loaded in some seconds.


## Milestones

- [x] Style transfer with VGG    **Files: VGG19deepstyle.ipynb**
- [x] Standard Deep Dreams with VGG  **Files: dreamerVGG.ipynb**
- [x] Standard Deep Dreams with Inception   **Files: dreamerInception.ipynb**
- [ ] Standard Deep Dreams with GANs
- [ ] Hacking with good ideas (Octaves, better loss functions)
- [x] Setting up datasets   **Files: Sounds.ipynb, Images.ipynb, imnetdl.py, sound.pkl**
- [ ] Retraining VGG to get new Dreams
- [ ] Retraining Inception to get new Dreams
- [ ] Training GAN to get new Dreams
- [ ] Training own CNN architectures to get new Dreams
- [ ] Training own CNN architectures to get audio style-transfer
- [ ] Training own CNN architectures to get audio Dreams
- [ ] Generating 2in1 Audio-visual dreams
- [ ] *Optional - Representation analysis and manipulation*
- [ ] Cleaning up code, packing it all together
- [ ] Final documentation

<!--
## Authors
* **Name1** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name2** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name3** - *Worked on.....* - [gitname](https://github.com/gitname)
!-->
