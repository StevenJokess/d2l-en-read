

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 23:08:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:33:54
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ashukid/Conditional-GAN-pytorch/blob/master/Conditional%20DCGAN.ipynb
-->
class DogDataset(torch.utils.data.Dataset):

    def __init__(self,all_images,annot_map,label_map,transform):
        self.all_images=all_images
        self.annot_map=annot_map
        self.label_map=label_map
        self.transform=transform

    def __getitem__(self,idx):

        impath=self.all_images[idx]
        image=Image.open(impath)

        # getting annotations for the image
        annotkey=impath.split("/")[-1].split(".")[0] # breednumber_imagenumber
        annot=self.annot_map[annotkey]

        labelkey=annot.split("/")[-2]
        temp=self.label_map[labelkey] # breednumber_breedname
        label=torch.zeros(120)
        label[temp]=1

        crop_size=self.getbbox(annot)
        image=image.crop(crop_size)

        return self.transform(image),label

    def __len__(self):
        return len(self.all_images)


    def getbbox(self,bpath):
        tree = ET.parse(bpath)
        root = tree.getroot()
        objects = root.findall('object')
        for o in objects:
            bndbox = o.find('bndbox') # reading bound box
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

        return (xmin,ymin,xmax,ymax)

---

https://github.com/anhtuan85/Generative-Adversarial-Networks-GANs-Specialization/blob/main/Course%203%20-%20Apply%20Generative%20Adversarial%20Networks%20(GANs)/Week%203/C3W3_Assignment.ipynb

# Inspired by https://github.com/aitorzip/PyTorch-CycleGAN/blob/master/datasets.py
class ImageDataset(Dataset):
    def __init__(self, root, transform=None, mode='train'):
        self.transform = transform
        self.files_A = sorted(glob.glob(os.path.join(root, '%sA' % mode) + '/*.*'))
        self.files_B = sorted(glob.glob(os.path.join(root, '%sB' % mode) + '/*.*'))
        if len(self.files_A) > len(self.files_B):
            self.files_A, self.files_B = self.files_B, self.files_A
        self.new_perm()
        assert len(self.files_A) > 0, "Make sure you downloaded the horse2zebra images!"

    def new_perm(self):
        self.randperm = torch.randperm(len(self.files_B))[:len(self.files_A)]

    def __getitem__(self, index):
        item_A = self.transform(Image.open(self.files_A[index % len(self.files_A)]))
        item_B = self.transform(Image.open(self.files_B[self.randperm[index]]))
        if item_A.shape[0] != 3:
            item_A = item_A.repeat(3, 1, 1)
        if item_B.shape[0] != 3:
            item_B = item_B.repeat(3, 1, 1)
        if index == len(self) - 1:
            self.new_perm()
        # Old versions of PyTorch didn't support normalization for different-channeled images
        return (item_A - 0.5) * 2, (item_B - 0.5) * 2

    def __len__(self):
        return min(len(self.files_A), len(self.files_B))

---

https://datawhalechina.github.io/dive-into-cv-pytorch/#/chapter02_image_classification_introduction/2.4_classification_action_SVHN/baseline

class SVHNDataset(Dataset):
    def __init__(self, img_path, img_label, transform=None):
        self.img_path = img_path
        self.img_label = img_label
        if transform is not None:
            self.transform = transform
        else:
            self.transform = None

    def __getitem__(self, index):
        img = Image.open(self.img_path[index]).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        lbl = np.array(self.img_label[index], dtype=np.int)
        lbl = list(lbl)  + (5 - len(lbl)) * [10]
        return img, torch.from_numpy(np.array(lbl[:5]))

    def __len__(self):
        return len(self.img_path)
