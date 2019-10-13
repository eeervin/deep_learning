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

Fancy def comes here

###Dataset2

Fancy def comes here

###Dataset3

Fancy def comes here

## Milestones

- [x] Style transfer with VGG
- [x] Standard Deep Dreams with VGG
- [x] Standard Deep Dreams with Inception
- [ ] Standard Deep Dreams with GANs
- [ ] Hacking with good ideas (Octaves, better loss functions)
- [ ] Setting up datasets
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


## Authors

* **Name1** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name2** - *Worked on.....* - [gitname](https://github.com/gitname)
* **Name3** - *Worked on.....* - [gitname](https://github.com/gitname)

