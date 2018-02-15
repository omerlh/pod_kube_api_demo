from kubernetes import client, config

config.load_incluster_config()
v1_core = client.CoreV1Api()
print(v1_core)