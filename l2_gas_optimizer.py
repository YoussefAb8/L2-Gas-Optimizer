import numpy as np
from sklearn.ensemble import RandomForestRegressor
import skl2onnx
from skl2onnx.common.data_types import FloatTensorType

# بيانات تجريبية بسيطة
X = np.array([[20.5, 12], [15.2, 14], [30.1, 18], [10.5, 3]], dtype=np.float32)
y = np.array([0.002, 0.0015, 0.004, 0.001], dtype=np.float32)

# تدريب الموديل
model = RandomForestRegressor(n_estimators=10)
model.fit(X, y)

# التحويل لـ ONNX
initial_type = [('float_input', FloatTensorType([None, 2]))]
onx = skl2onnx.convert_sklearn(model, initial_types=initial_type)

with open("gas_optimizer.onnx", "wb") as f:
    f.write(onx.SerializeToString())

print("✅ Success! gas_optimizer.onnx has been created.")
