class BinaryNumber:

    def __init__(self, value):
        if isinstance(value, str):
            self.value = int(value, 2)
        else:
            self.value = value

    def __str__(self):
        return bin(self.value)[2:]

    def and_operation(self, other):
        return BinaryNumber(self.value & other.value)

    def or_operation(self, other):
        return BinaryNumber(self.value | other.value)

    def xor_operation(self, other):
        return BinaryNumber(self.value ^ other.value)

    def invert(self):
        num_bits = self.value.bit_length()
        mask = (1 << num_bits) - 1
        return BinaryNumber(~self.value & mask)

if __name__ == "__main__":
    bin_num1 = BinaryNumber("1010")
    bin_num2 = BinaryNumber("1100")

    print("Число 1: ", bin_num1)

    print("AND: ", bin_num1.and_operation(bin_num2))
    print("OR: ", bin_num1.or_operation(bin_num2))
    print("XOR: ", bin_num1.xor_operation(bin_num2))
    print("NOT число 1: ", bin_num1.invert())
