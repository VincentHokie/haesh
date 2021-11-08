import random
import math

class Haesh(object):

    def __init__(self):
        self.digest = []
        self._expansion_value = 2**8
        self.expansion_permutation = [index for index in range(self._expansion_value)]
        self.iteration = 0

    def calculate_digest(self, last_cipherblock):
        self._expand_and_recalculate_digest(last_cipherblock)
    
    def _expand_and_recalculate_digest(self, last_cipherblock):
        expanded_cipherblock = self._expand_cipherblock(last_cipherblock)
        if not self.digest:
            self.digest = expanded_cipherblock

        # xor the current digest with the new expanded cipherblock
        self.digest = [ (int(p) ^ int(l)) for (p, l) in zip(self.digest, expanded_cipherblock) ]

    def _expand_cipherblock(self, last_cipherblock):

        # use last cipherblock to determine shuffle of expansion_permutation that will
        # determine how the 128 bits turn to 512 bits
        ord_list = [str(char) for char in last_cipherblock]
        ord_string = "".join(ord_list)
        random.seed(int(ord_string))
        random.shuffle(self.expansion_permutation)

        # convert character string to bit string
        last_cipherblock_bits = "".join(['{0:08b}'.format(char) for char in last_cipherblock])

        # expand 128 bit cipherblock to 512 bits, by mapping every 2 bits to 8 bits
        SAMPLE_SIZE = 2
        no_of_blocks = math.ceil(len(last_cipherblock_bits)/SAMPLE_SIZE)
        expanded_ords = []

        for block_index in range(no_of_blocks):
            # these additions need to be mod 64
            first_index = self._iteration_addition(block_index, 62)
            first_bit = last_cipherblock_bits[first_index]
            second_bit = last_cipherblock_bits[first_index + 1]
            index = int(f'{first_bit}{second_bit}', 2) + block_index
            expanded_ords.append('{:02}'.format(self.expansion_permutation[index % self._expansion_value]))

        # ensure next iteration creates an offset in the values we pick from
        # expansion_permutation for expansion, this needs to be mod 64
        self.iteration = self._iteration_addition(1)
        return expanded_ords

    def get_hex_digest(self):
        return '%08X' % int("".join(['{0:08b}'.format(char) for char in self.digest]), 2)

    def _iteration_addition(self, additive, mod = 64):
        return (self.iteration + additive) % (mod or self._expansion_value)
