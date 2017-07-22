import re


class Parser(object):
    def __init__(self, input):
        self.input = input
        self.output = []

    def parse(self):
        for line in self.input:
            if re.match('\w', line):
                self.output.append(
                    re.split(r' *', re.sub('\n|[^A-Za-z0-9\s]', '', line)))
            else:
                pass

        return self.output

    def get_max_lengths(self):
        longest_sentence = max(self.output)
        max_lengths = [0 for word in longest_sentence]

        for sentence in self.output:
            for idx, token in enumerate(sentence):
                current_token_length = len(token)
                if max_lengths[idx] < current_token_length:
                    max_lengths[idx] = current_token_length

        return max_lengths

if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        parser = Parser(input)
        for s in parser.parse():
            print s

        print '\n' + '=' * 75 + '\n'

        max_lengths = parser.get_max_lengths()
        print max_lengths


        # Format output as table
        pattern = ''
        parsed = parser.parse()
        for sentence in parsed:
            for idx, word in enumerate(sentence):
                pattern += '%-' + str(max_lengths[idx] + 3) + 's'
            print pattern

            s = tuple(sentence)
            # print s
            print pattern % s
            pattern = '';
