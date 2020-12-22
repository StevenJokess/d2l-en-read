# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-23 00:03:12
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-23 00:04:27
Description:
TODO::
Reference:https://pytorch.org/docs/master/notes/serialization.html#recommended-approach-for-saving-a-model
'''
# A module with control flow
class ControlFlowModule(torch.nn.Module):
    def __init__(self):
        super(ControlFlowModule, self).__init__()
        self.l0 = torch.nn.Linear(4, 2)
        self.l1 = torch.nn.Linear(2, 1)

    def forward(self, input):
        if input.dim() > 1:
            return torch.tensor(0)

        out0 = self.l0(input)
        out0_relu = torch.nn.functional.relu(out0)
        return self.l1(out0_relu)

>>> traced_module = torch.jit.trace(ControlFlowModule(), torch.randn(4))
>>> torch.jit.save(traced_module, 'controlflowmodule_traced.pt')
>>> loaded = torch.jit.load('controlflowmodule_traced.pt')
>>> loaded(torch.randn(2, 4)))
tensor([[-0.1571], [-0.3793]], grad_fn=<AddBackward0>)

>>> scripted_module = torch.jit.script(ControlFlowModule(), torch.randn(4))
>>> torch.jit.save(scripted_module, 'controlflowmodule_scripted.pt')
>>> loaded = torch.jit.load('controlflowmodule_scripted.pt')
>> loaded(torch.randn(2, 4))
tensor(0)
