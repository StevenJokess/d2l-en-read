7. Generative Adversarial Networks
Activity 7.01: Implementing a DCGAN for the MNIST Fashion Dataset
Solution
Open a new Jupyter Notebook and name it Activity 7.01. Import the following library packages:
# Import the required library functions

import numpy as np

import matplotlib.pyplot as plt

from matplotlib import pyplot

import tensorflow as tf

from tensorflow.keras.layers import Input

from tensorflow.keras.initializers import RandomNormal

from tensorflow.keras.models import Model, Sequential

from tensorflow.keras.layers \

import Reshape, Dense, Dropout, Flatten,Activation

from tensorflow.keras.layers import LeakyReLU,BatchNormalization

from tensorflow.keras.layers import Conv2D, UpSampling2D,Conv2DTranspose

from tensorflow.keras.datasets import fashion_mnist

from tensorflow.keras.optimizers import Adam

Create a function that will generate real data samples from the fashion MNIST data:
# Function to generate real data samples

def realData(batch):

    # Get the MNIST data

    (X_train, _), (_, _) = fashion_mnist.load_data()

    # Reshaping the input data to include channel

    X = X_train[:,:,:,np.newaxis]

    # normalising the data to be between 0 and 1

    X = (X.astype('float32') - 127.5)/127.5

    # Generating a batch of data

    imageBatch = X[np.random.randint(0, X.shape[0], \

                                     size=batch)]

    return imageBatch

The output from this function is the batch of MNIST data. Please note that we normalize the input data by subtracting 127.5, which is half the max pixel value, and dividing by the same value. This will help in converging the solution faster.

Now, let's generate a set of images from the MNIST dataset:
# Generating a set of sample images

fashionData = realData(25)

You should get the following output:

Figure 7.36: Generating images from MNIST
Figure 7.36: Generating images from MNIST

Now, let's visualize the images with matplotlib:
# for j in range(5*5):

    pyplot.subplot(5,5,j+1)

    # turn off axis

    pyplot.axis('off')

    pyplot.imshow(fashionData[j,:,:,0],cmap='gray_r')

You should get an output similar to the one shown here:

Figure 7.37: Plotted images
Figure 7.37: Plotted images

From the output, we can see the visualization of several fashion articles. We can see that the images are centrally located within a white background. This are the images that we'll try to recreate.

Now, let's define the function to generate inputs for the generator network. The inputs are random data points that are generated from a random uniform distribution:
# Function to generate inputs for generator function

def fakeInputs(batch,infeats):

    # Generate random noise data with shape (batch,input features)

    x_fake = np.random.uniform(-1,1,size=[batch,infeats])

    return x_fake

This function generates the fake data that was sampled from the random distribution as the output.

Let's define the function for building the generator network:
Activity7.01.ipynb

# Function for the generator model

def genModel(infeats):

    # Defining the Generator model

    Genmodel = Sequential()

    Genmodel.add(Dense(512,input_dim=infeats))

    Genmodel.add(Activation('relu'))

    Genmodel.add(BatchNormalization())

    # second layer of FC => RElu => BN layers

    Genmodel.add(Dense(7*7*64))

    Genmodel.add(Activation('relu'))

    Genmodel.add(BatchNormalization())

The complete code for this step can be found at https://packt.live/3fpobDm

Building the generator network is similar to building any CNN network. In this generator network, we will use the transpose convolution method for upsampling images. In this model, we can see the progressive use of the transpose convolution. The initial input starts with a dimension of 100, which is our input feature. The dimension of the MNIST dataset is batch size x 28 x 28. Therefore, we have upsampled the data twice to get the output as batch size x 28 x 28.

Next, we define the function that will be used to create fake samples:
# Function to create fake samples using the generator model

def fakedataGenerator(Genmodel,batch,infeats):

    # first generate the inputs to the model

    genInputs = fakeInputs(batch,infeats)

    """

    use these inputs inside the generator model \

    to generate fake distribution

    """

    X_fake = Genmodel.predict(genInputs)

    return X_fake

In this function, we only return the X variable. The output from this function is the fake dataset.

Define the parameters that we will use in many of the functions, along with the summary of the generator network:
# Define the arguments like batch size and input feature

batch = 128

infeats = 100

Genmodel = genModel(infeats,)

Genmodel.summary()

You should get the following output:

Figure 7.38: Summary of the generative model
Figure 7.38: Summary of the generative model

From the summary, please note how the dimension of the input noise changes with each transpose convolution operation. Finally, we get an output that is equal in dimension to the real dataset, ( None,28 ,28,1).

Let's use the generator function to generate a fake sample before training:
# Generating a fake sample and printing the shape

fake = fakedataGenerator(Genmodel,batch,infeats)

fake.shape

You should get the following output:

(128, 28, 28, 1)

Now, let's plot the generated fake sample:
# Plotting the fake sample

plt.imshow(fake[1, :, :, 0], cmap='gray_r')

You should get an output similar to the following:

Figure 7.39: Output of the fake sample
Figure 7.39: Output of the fake sample

This is the plot of the fake sample before training. After training, we want samples like these to look like the MNIST fashion samples we visualized earlier in this activity.

Build the discriminator model as a function. The network architecture will be similar to a CNN architecture:
Activity7.01.ipynb

# Descriminator model as a function

def discModel():

    Discmodel = Sequential()

    Discmodel.add(Conv2D(32,kernel_size=(5,5),strides=(2,2),\

                  padding='same',input_shape=(28,28,1)))

    Discmodel.add(LeakyReLU(0.2))

    # second layer of convolutions

    Discmodel.add(Conv2D(64, kernel_size=(5,5), strides=(2, 2), \

                  padding='same'))

    Discmodel.add(LeakyReLU(0.2))

The full code for this step can be found at https://packt.live/3fpobDm

In the discriminator network, we have included all the necessary layers, such as the convolutional operations and LeakyReLU. Please note that the last layer is a sigmoid layer as we want the output as a probability of whether the sample is real (1) or fake (0).

Print the summary of the discriminator network:
# Print the summary of the discriminator model

Discmodel = discModel()

Discmodel.summary()

You should get the following output:

Figure 7.40: Discriminator model summary
Figure 7.40: Discriminator model summary

Define the GAN model as a function:
# Define the combined generator and discriminator model, for updating the generator

def ganModel(Genmodel,Discmodel):

    # First define that discriminator model cannot be trained

    Discmodel.trainable = False

    Ganmodel = Sequential()

    # First adding the generator model

    Ganmodel.add(Genmodel)

    """

    Next adding the discriminator model

    without training the parameters

    """

    Ganmodel.add(Discmodel)

    """

    Compile the model for loss to optimise the Generator model

    """

    Ganmodel.compile(loss='binary_crossentropy',\

                     optimizer = 'adam')

    return Ganmodel

The structure of the GAN model is similar to the one we developed in Exercise 7.05, Implementing the DCGAN.

Now, it's time to invoke the GAN function:
# Initialise the GAN model

gan_model = ganModel(Genmodel,Discmodel)

# Print summary of the GAN model

gan_model.summary()

Please note that the inputs to the GAN model are the previously defined generator model and the discriminator model. You should get the following output:

Figure 7.41: GAN model summary
Figure 7.41: GAN model summary

Please note that the parameters of each layer of the GAN model are equivalent to the parameters of the generator and discriminator models. The GAN model is just a wrapper around the two models we defined earlier.

Define the number of epochs to train the network on using the following code:
# Defining the number of epochs

nEpochs = 5000

Now, we can start the process of training the network:
Note:

Before you run the following code, make sure you have created a folder called output in the same path as your Jupyter Notebook.

Activity7.01.ipynb

# Train the GAN network

for i in range(nEpochs):

    """

    Generate samples equal to the batch size

    from the real distribution

    """

    x_real = realData(batch)

    #Generate fake samples using the fake data generator function

    x_fake = fakedataGenerator(Genmodel,batch,infeats)

    # Concatenating the real and fake data

    X = np.concatenate([x_real,x_fake])

    #Creating the dependent variable and initializing them as '0'

    Y = np.zeros(batch * 2)

The complete code for this step can be found on https://packt.live/3fpobDm

It needs to be noted here that the training of the discriminator model with the fake and real samples and the training of the GAN model happens concurrently. The only difference is the training of the GAN model proceeds without updating the parameters of the discriminator model. The other thing to note is that, inside the GAN, the labels for the fake samples would be 1 to generate large loss terms that will be backpropagated through the discriminator network to update the generator parameters. We also display the predicted probability of the GAN for every 50 epochs. When calculating the probability, we combine a sample of real data and a sample of fake data and then take the mean of the predicted probability. We also save a copy of the generated image.

You should get an output similar to the following:

Discriminator probability:0.5276428461074829

Discriminator probability:0.5038391351699829

Discriminator probability:0.47621315717697144

Discriminator probability:0.48467564582824707

Discriminator probability:0.5270703434944153

Discriminator probability:0.5247280597686768

Discriminator probability:0.5282968282699585

Let's also look at some of the plots that were generated from the training process at various epochs:

Figure 7.42: Images generated during the training process
Figure 7.42: Images generated during the training process

From the preceding plots, we can see the progression of the training process. We can see that by epoch 100, the plots were mostly noise. By epoch 600, the forms of the fashion articles started to become more pronounced. At epoch 1,500, we can see that the fake images are looking very similar to the fashion dataset.

Note:

You can take a closer look at these images by going to https://packt.live/2W1FjaI.

Now, let's look at the images that were generated after training:
# Images generated after training

x_fake = fakedataGenerator(Genmodel,25,infeats)

# Displaying the plots

for j in range(5*5):

pyplot.subplot(5,5,j+1)

    # turn off axis

    pyplot.axis('off')

    pyplot.imshow(x_fake[j,:,:,0],cmap='gray_r')

You should get an output similar to the following:

Figure 7.43: Images generated after the training process
Figure 7.43: Images generated after the training process

From the training accuracy levels, you can see that the accuracy of the discriminator model hovers around the .50 range, which is the desired range. The purpose of the generator is to create fake images that look like real ones. When the generator generates images that look very similar to real images, the discriminator gets confused as to whether the image has been generated from the real distribution or fake distribution. This phenomenon manifests in an accuracy level of around 50% for the discriminator, which is the desired level.

Note

To access the source code for this specific section, please refer to https://packt.live/3fpobDm.

This section does not currently have an online interactive example, and will need to be run locally.

[1]: https://learning.oreilly.com/library/view/the-deep-learning/9781839219856/B15385_Solution_Final_RK_ePub.xhtml#_idParaDest-258
