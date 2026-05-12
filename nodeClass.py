from pinCalls import *
class outputNode:
    prompt = ""
    outputs = []
    children = {}

    def add_output(self, output: [pins,pinState]):
        self.outputs.append(output)

    def add_child(self, keys: [list[str],'outputNode']):
        for key in keys[0]:
            print(f"key is: {key}")
            self.children[key] = keys[1]

    def add_prompt(self, newprompt: str):
        prompt = newprompt


class outputNodeTest:
    prompt = ""
    outputs = []
    children = {}



    def add_child(self, keys: [list[str],'outputNode']):
        for key in keys[0]:
            print(f"key is: {key}")
            self.children[key] = keys[1]

    def add_prompt(self, newprompt: str):
        prompt = newprompt



start = outputNodeTest()
start.add_prompt("Hello")
fire = outputNodeTest()
water = outputNodeTest()
try:
    start.add_child([["Fire","Left","Heat"],fire])
finally:
    print(start.children)