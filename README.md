# Pod k8s API Demo
I did this small POC to learn how a pod access the k8s API. 
You can read more about it in the [documentation](https://kubernetes.io/docs/admin/authentication/#service-account-tokens).
To run it, use local k8s deployment (minikube for example). 
Do not run this on a production cluster - the code will change labels on the nodes.
After setting up the cluster, simply run:
```
kubectl apply -f .
```

And than use `kubectl get nodes`, to see the new label apply to the nodes.

The code here is based upon this [example](https://github.com/kubernetes-client/python/blob/master/examples/manage_node_labels.py), from the official k8s python client repository.