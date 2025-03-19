# Generative Adversarial Networks (GANs)

Welcome to the **Generative Adversarial Networks (GANs)** section! This folder provides an introduction to GANs, a class of deep learning models used for generating realistic synthetic data. GANs consist of two neural networks, a **Generator** and a **Discriminator**, that compete in a game-theoretic framework to improve data generation quality.

**Note**: The notebooks here introduce foundational GAN concepts but do not cover all advanced variations. For a more comprehensive understanding, please refer to the recommended resources provided below.

---

## 📂 Structure

This folder currently includes:
  - **PyTorch Implementation**: A simple GAN trained on the Fashion MNIST dataset and GAN Architectures that explore the implementations of common GAN architectures such as DCGAN and WGAN in PyTorch.
  - **TensorFlow Implementation**: A GAN-based model to generate realistic masked face images using various GAN architectures like Inception V2, Xception and others
Each section includes **assignments** to reinforce learning, along with **solutions** for self-assessment.

---

## 🔗 Learning Flow

Follow these steps to build a strong foundation in GANs:

### 1. **Fashion MNIST GAN (PyTorch)**
- **Purpose**: Train a simple GAN to generate realistic images of Fashion MNIST clothing items.
- **Topics to Cover**:
  - Generator and Discriminator networks
  - Training loop and adversarial loss
  - Evaluating GAN-generated images
- **Resources**:
  - [PyTorch DCGAN Tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)
  - [Fashion MNIST Dataset](https://github.com/zalandoresearch/fashion-mnist)
  - [GANs Explained (Stanford CS231n)](http://cs231n.stanford.edu/reports/2017/pdfs/161.pdf)

### 3. **CNN-Based Mask Detection GAN (TensorFlow)**
- **Purpose**: Use Convolutional Neural Networks to implement a model that detects whether a person is wearing a mask.
- **Topics to Cover**:
  - CNN-based GAN training
  - Data augmentation with synthetic images
- **Resources**:
  - [TensorFlow GANs Guide](https://www.tensorflow.org/tutorials/generative/dcgan)
  - [Face Mask Dataset](https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset)


## 📝 Assignments and Solutions

Each GAN model includes hands-on assignments designed to help you apply what you've learned. Solutions are provided for self-evaluation. Try to complete the assignments independently before checking the solutions for the best learning experience.

---

## 🏁 Getting Started

1. **Begin with Fashion MNIST GAN (PyTorch)**: Understand how basic GANs generate synthetic images.
3. **Move to TensorFlow: Mask Detection GAN**: Use GANs for augmenting masked face datasets.

---

Happy coding! Developing GANs will enable you to generate high-quality synthetic data and explore creative AI applications. For further learning, refer to the documentation and tutorials linked above.
