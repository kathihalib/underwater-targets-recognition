import onnx

model = onnx.load("last.onnx")
input_all = [node.name for node in model.graph.input]

print("模型输入节点名称:", input_all)