from kubernetes import client, config

config.load_incluster_config()
api_instance = client.CoreV1Api()

body = {
    "metadata": {
        "labels": {
            "foo": "bar",
            "baz": None}
    }
}

api_response = api_instance.patch_node("minikube", body)

print(api_response)