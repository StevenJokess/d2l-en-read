

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-21 23:14:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 21:46:49
 * @Description:
 * @TODO::
 * @Reference:[1]: https://blog.csdn.net/weixin_38145317/article/details/103582549
 *[2]: https://github.com/kuangliu/pytorch-cifar/blob/master/main.py
 [3]: https://github.com/0809zheng/pokemon-DCGAN-pytorch/blob/master/gan.py
 [4]: https://github.com/lyhue1991/eat_pytorch_in_20_days/blob/master/6-3%2C%E4%BD%BF%E7%94%A8GPU%E8%AE%AD%E7%BB%83%E6%A8%A1%E5%9E%8B.md
-->
pytorch 模型 .pt, .pth, .pkl的区别及模型保存方式

我们经常会看到后缀名为.pt, .pth, .pkl的pytorch模型文件，这几种模型文件在格式上有什么区别吗？其实它们并不是在格式上有区别，只是后缀不同而已（仅此而已），在用torch.save()函数保存模型文件时，各人有不同的喜好，有些人喜欢用.pt后缀，有些人喜欢用.pth或.pkl.用相同的torch.save（）语句保存出来的模型文件没有什么不同。

在pytorch官方的文档/代码里，有用.pt的，也有用.pth的。一般惯例是使用.pth,但是官方文档里貌似.pt更多，而且官方也不是很在意固定用一种。

模型保存与调用方式一：

保存：

torch.save(model.state_dict(), mymodel.pth)#只保存模型权重参数，不保存模型结构

调用：

model = My_model(*args, **kwargs)  #这里需要重新模型结构，My_model
model.load_state_dict(torch.load(mymodel.pth))#这里根据模型结构，调用存储的模型参数
model.eval()

模型保存与调用方式一：

保存：

torch.save(model, mymodel.pth)#保存整个model的状态

调用：

model=torch.load(mymodel.pth)#这里已经不需要重构模型结构了，直接load就可以
model.eval()

---
[2]
    if acc > best_acc:
        print('Saving..')
        state = {
            'net': net.state_dict(),
            'acc': acc,
            'epoch': epoch,
        }
        if not os.path.isdir('checkpoint'):
            os.mkdir('checkpoint')
        torch.save(state, './checkpoint/ckpt.pth')
        best_acc = acc
---
[3]
    if (e+1) % 5 == 0:
        torch.save(G.state_dict(), os.path.join(workspace_dir, f'dcgan_g.pth'))
        torch.save(D.state_dict(), os.path.join(workspace_dir, f'dcgan_d.pth'))

---
[4]
# save the model parameters
torch.save(model.net.module.state_dict(), "model_parameter.pkl")
