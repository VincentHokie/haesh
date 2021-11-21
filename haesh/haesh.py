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
            return

        # xor the current digest with the new expanded cipherblock
        self.digest = [ (int(p) ^ int(l)) for (p, l) in zip(self.digest, expanded_cipherblock) ]

    def _expand_cipherblock(self, last_cipherblock):

        # use last cipherblock to determine shuffle of expansion_permutation that will
        # determine how the 128 bits turn to 512 bits
        ord_list = [str(char) for char in last_cipherblock]
        ord_string = "".join(ord_list)
        random.seed(int(ord_string))

        # current #1 performance bottleneck
        random.shuffle(self.expansion_permutation)

        # expand 128 bit cipherblock to 512 bits, by mapping every 8 bits to 24 bits
        expanded_ords = []

        for block_index in last_cipherblock:
            first_index = (block_index + self.iteration) % self._expansion_value
            # this addition needs to be mod 256 so that we pick a value within the array
            expanded_ords.extend([self.expansion_permutation[first_index], self.expansion_permutation[(first_index + 1) % self._expansion_value], self.expansion_permutation[(first_index + 2) % self._expansion_value] ])

        # ensure next iteration creates an offset in the values we pick from
        # expansion_permutation for expansion
        self.iteration += 1
        return expanded_ords

    def get_hex_digest(self):
        return '%08X' % int("".join(['{0:08b}'.format(char) for char in self.digest]), 2)
