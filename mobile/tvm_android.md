

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 19:39:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-10 19:40:16
 * @Description:
 * @TODO::
 * @Reference:
-->
# Deploy to Android[1]
Build model for Android Target
Relay compilation of model for android target could follow same approach like android_rpc. The code below will save the compilation output which is required on android target.

```
lib.export_library("deploy_lib.so", ndk.create_shared)
with open("deploy_graph.json", "w") as fo:
    fo.write(graph.json())
with open("deploy_param.params", "wb") as fo:
    fo.write(relay.save_param_dict(params))
deploy_lib.so, deploy_graph.json, deploy_param.params will go to android target.
```

# TVM Runtime for Android Target

Refer here to build CPU/OpenCL version flavor TVM runtime for android target. From android java TVM API to load model & execute can be referred at this java sample source.
[1]: https://tvm.apache.org/docs/deploy/android.html
