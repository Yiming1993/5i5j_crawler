import config
import re

def clean_marks(sentence, clean_type = 'raw'):
    f = open(config.origin_path() + '/References/stop.txt').readlines()
    mark_list = [i.strip() for i in f]
    sentence = ''.join([i for i in sentence if i not in mark_list])
    if clean_type == 'raw':
        return sentence
    if clean_type == 'clear':
        if '.' in sentence and sentence[-1] == '.' and sentence != 'e.g.':
            sentence = sentence[:-1]
        return sentence
    if clean_type == 'ultimate':
        if '.' in sentence and sentence[-1] == '.':
            sentence = sentence[:-1]
        sentence = sentence.lower()
        return sentence
    else:
        raise ValueError('no idea how to clean the sentence')

def format_control(string, control_list):
    string = re.sub(control_list[0], control_list[1], str(string))
    return string