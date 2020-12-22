

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 11:57:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 11:57:12
 * @Description:
 * @TODO::
 * @Reference:https://github.com/kazizzad/DCGAN-Gluon-MxNet/blob/master/MxnetDCGAN.ipynb
-->

class Options:
    def __init__(self):
        self.dataset = 'celebA' # cifar10 , celebA
        #self.dataroot = '/EBS100G/GAN_resutls/lfw/lfw-deepfunneled' # path to dataset
        self.dataroot = './data' # path to dataset
        self.batchSize = 64 # input batch size
        self.imageSize = 64 # the height / width of the input image to network'
        self.nz =100 # size of the latent z vector
        self.ngf = 64
        self.ndf = 64
        self.nc = 3 #numb color
        self.niter =125 # number of epochs to train for
        self.lr = 0.0001 # learning rate, default=0.0002
        self.beta1 = 0.5 # beta1 for adam
        self.beta2 = 0.999 # beta2 for adam
        self.ctx = mx.gpu() #  enables gpu
        self.ngpu = 1 # number of GPUs to use
#         self.G_net = '' # path to netG (to continue training)
#         self.D_net = '' #help="path to netD (to continue training)")
        self.outf = './data' # help='folder to output images and model checkpoints')
        self.manualSeed = random.randint(1, 10000) # manual seed
        self.clip_gradient = 10.0

opt = Options()
try:
    os.makedirs(opt.outf)
except OSError:
    pass
