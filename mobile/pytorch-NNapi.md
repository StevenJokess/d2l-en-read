

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-28 17:23:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-28 17:35:36
 * @Description:
 * @TODO::
 * @Reference:https://www.youtube.com/watch?v=B-2spa3UCTU
-->

CPU GPU NPU DSP

my_model = trace_or_load_model()

input = torch.zeros(input_shape)
# Optional. Teslls NNAPI to use NHWC/
input.nnapi_nhwc = True

# Convert model. One line.
nnapi_model = torch.backends._nnapi.prepare \
.convert_model_to_nnapi(my_model, input)

# Optional. Makes benchmarking easier.
torch.utils.bundled_inputs \
.augment_model_with_bundled_inputs(nnapi_model, [(input,)])

nnapi_model.save(output_path)

RUNNING YOUR MODEL

Benchmark model on device
./speed_benchmark_torch --model=my_model.pt --use_bundled_input=0

Use the model in an app
# No code changes needed. Just replace your existing model with the NNAPI model

---

Initial release

- Android 10+
- Linear Convolution model e.g FBNet
- Multi-Layer Perceptron models

---

WHAT's COMING UP

- Addtional operator types
- Mask R-CNN model support
- Fallback to optimised CPU
- Android support back to 8(Oreo) and 9(Pie)
- Control flow semantics

---

- Download PyTorch Moble nightly build
- Try out the code
- Providee feedback

---

developer.android.com/ndk/guides/neuralnetworks
pytorch.org/mobile/android
