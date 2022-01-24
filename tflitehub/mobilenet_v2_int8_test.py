# RUN: %PYTHON %s

import absl.testing
import numpy
import test_util

model_path = "https://storage.googleapis.com/tf_model_garden/vision/mobilenet/v2_1.0_int8/mobilenet_v2_1.00_224_int8.tflite"

class MobilenetV2Int8Test(test_util.TFLiteModelTest):
  def __init__(self, *args, **kwargs):
    super(MobilenetV2Int8Test, self).__init__(model_path, *args, **kwargs)

  def compare_results(self, iree_results, tflite_results, details):
    super(MobilenetV2Int8Test, self).compare_results(iree_results, tflite_results, details)
    self.assertTrue(numpy.isclose(iree_results[0], tflite_results[0], atol=1.0).all())

  def test_compile_tflite(self):
    self.compile_and_execute()

if __name__ == '__main__':
  absl.testing.absltest.main()

