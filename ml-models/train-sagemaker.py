import sagemaker
from sagemaker.tensorflow import TensorFlow

# Orchestrating SageMaker training (Professional Experience: AWS Developer) [cite: 8]
tf_estimator = TensorFlow(
    entry_point='lstm_model.py',
    role=sagemaker.get_execution_role(),
    instance_count=1,
    instance_type='ml.p3.2xlarge', # High-performance GPU instance
    framework_version='2.11',
    py_version='py39',
    script_mode=True
)

tf_estimator.fit({'training': 's3://aegis-ml-data/train'})