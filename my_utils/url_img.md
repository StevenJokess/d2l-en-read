

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-14 22:16:15
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 22:16:29
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/vijishmadhavan/Light-Up/blob/master/ArtLine(Try_it_on_Colab).ipynb#scrollTo=DjlZYFlZcK6Q
-->
url = 'https://art19.com/shows/the-beat-with-ari-melber' #@param {type:"string"}

response = requests.get(url)
img = PIL.Image.open(BytesIO(response.content)).convert("RGB")
img_t = T.ToTensor()(img)
img_fast = Image(img_t)
show_image(img_fast, figsize=(7,7), interpolation='nearest');
