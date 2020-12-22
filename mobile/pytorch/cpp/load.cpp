

/*
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-23 00:01:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-23 00:02:19
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/docs/master/notes/serialization.html#recommended-approach-for-saving-a-model
 * https://pytorch.org/cppdocs/
 */
torch::jit::script::Module module;
module = torch::jit::load('controlflowmodule_scripted.pt');
