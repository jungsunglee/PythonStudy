#raise
try:
    numNeagtive = int(input("Input the negative number : "))
    if numNeagtive >= 0:
        raise Exception("ERROR of Positive Number")
except Exception as e:
    print("[ERROR]", e)

try:
    numNeagtive = int(input("Input the negative number : "))
    if numNeagtive >= 0:
        raise ValueError("ERROR of Positive Number")
except ValueError as e:
    print("[ERROR]", e)

# ERROR Generate
class PsitiveNumerERROR(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

try:
    numNeagtive = int(input("Input the negative number : "))
    if numNeagtive >= 0:
        raise PsitiveNumerERROR("ERROR of Positive Number")

except PsitiveNumerERROR as e:
    print("[ERROR]", e)