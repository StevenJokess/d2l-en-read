

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 21:13:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-07 23:13:08
 * @Description:
 * @TODO::
 * @Reference:https://www.tensorflow.org/tutorials/generative/cvae
-->
Display an animated GIF of all the saved images

```py
anim_file = 'cvae.gif'


with imageio.get_writer(anim_file, mode='I') as writer:
  filenames = glob.glob('image*.png')
  filenames = sorted(filenames)
  for filename in filenames:
    image = imageio.imread(filename)
    writer.append_data(image)
  image = imageio.imread(filename)
  writer.append_data(image)

import tensorflow_docs.vis.embed as embed
embed.embed_file(anim_file)
```

---

```py
from visual import save_gan, cvt_gif
cvt_gif(gan)
```

```py
# [3]
def cvt_gif(folders_or_gan):
    if not isinstance(folders_or_gan, list):
        folders_or_gan = [folders_or_gan.__class__.__name__.lower()]
    for folder in folders_or_gan:
        folder = "visual/"+folder
        fs = [folder+"/" + f for f in os.listdir(folder)]
        imgs = []
        for f in sorted(fs, key=os.path.getmtime):
            if not f.endswith(".png"):
                continue
            try:
                int(os.path.basename(f).split(".")[0])
            except ValueError:
                continue
            img = Image.open(f)
            img = img.resize((img.width//10, img.height//10), Image.ANTIALIAS)
            imgs.append(img)
        path = "{}/generating.gif".format(folder)
        if os.path.exists(path):
            os.remove(path)
        imgs[-1].save(path, append_images=imgs, optimize=False, save_all=True, duration=400, loop=0)
        print("saved ", path)
```

[3]: https://github.com/MorvanZhou/mnistGANs/blob/main/visual.py
