# to import module test that is located in module test folder(the other folder)
# Added the below command to the settings.json file
# "python.analysis.extraPaths":["./basicPython/moduleTest"],

version = 2.0
def printAuth():
    print("func_module_test")

class pay:
    def __init__(self, id, price, time) -> None:
        self.id = id
        self.price = price
        self.time = time
    
    def get_pay_info(self):
        return f"{self.id}"

if __name__ == "__main__":
    print(__name__)