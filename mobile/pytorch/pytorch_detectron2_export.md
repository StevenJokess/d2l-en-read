

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-13 23:05:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-13 23:06:07
 * @Description:
 * @TODO::
 * @Reference:https://detectron2.readthedocs.io/_modules/detectron2/export/api.html#Caffe2Tracer.export_torchscript
-->

    def export_torchscript(self):
        """
        Export the model to a ``torch.jit.TracedModule`` by tracing.
        The returned object can be saved to a file by ``.save()``.

        Returns:
            torch.jit.TracedModule: a torch TracedModule
        """
        model, inputs = self._get_traceable()
        logger = logging.getLogger(__name__)
        logger.info("Tracing the model with torch.jit.trace ...")
        with torch.no_grad():
            return torch.jit.trace(model, (inputs,))
