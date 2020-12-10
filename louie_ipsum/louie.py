import random
import re

# generic template processing, separate this into another module
class GenericIpsum(object):

    def __init__(self):
        self.tag_re = re.compile(r'\[(.+?)\]')

        # change these - might not need to be res
        self.num_range_re = re.compile(r'([0-9]+)-([0-9]+)')
        self.literal_list_re = re.compile(r"('[^']+',\s*)+'[^']+'")
        self.literal_list_split_re = re.compile(r'\W+')

    def num_range(self, min_num, max_num):
        num_list = list(range(min_num, max_num + 1))
        return str(random.choice(num_list))

    def literal_list(self, list_str):
        split_elems = re.split(self.literal_list_split_re, list_str)
        literal_elem_list = [elem for elem in split_elems if elem != '']
        return random.choice(literal_elem_list)

    def term(self, term_str):
        term_choice_list = self.terms[term_str]

        return random.choice(term_choice_list)

    def process_tag(self, m):
        inner_str = m.group(1)
        
        inner_m = self.num_range_re.match(inner_str)
        if inner_m:
            return self.num_range(int(inner_m.group(1)), int(inner_m.group(2)))
 
        inner_m = self.literal_list_re.match(inner_str)
        if inner_m:
            return self.literal_list(inner_str)

        else:
            return self.term(inner_str)
        
    def process_fragment(self, frag_str):
        return self.tag_re.sub(self.process_tag, frag_str)

    def get(self):
        ret_str_list = []

        for cur_frag_list in self.fragments:
            cur_frag = random.choice(cur_frag_list)
            proc_frag = self.process_fragment(cur_frag)
            ret_str_list.append(proc_frag)

        return '. '.join(ret_str_list)
 
    def __iter__(self):
        return self

    def __next__(self):
        return self.get() 


class LouieIpsum(GenericIpsum):

    fragments = [
        [
            "We got [westside_lifter] to a [700-1000] pound [main_lift] with [4-8] weeks of ['max','dynamic'] effort [special_exercise]",
            "I broke my ['lower back','patella','forearm'] in [1971-2008] on a max effort [special_exercise]",
            "I spoke to [famous_lifter] at ['USPF','AAU','APF','SPF'] Senior Nationals, and he told me",
            "These fuckin' geeks ain't never done a [main_lift] in their life and they wanna tell me about gettin stronger",
        ],
        [
            "You know the Russians, they've been doing this since the 1950s",
            "If you got weak [muscle_group], you can't do a [main_lift], that's a basic fact of physics",
            "Force equals mass times acceleration",
            "It's not against the rules to take drugs, it's against the rules to get caught takin' drugs",
            "Bands and chains provide accommodating resistance",
        ],
        [
            "We use equipment, just like a baseball player uses a bat",
            "You rotate the special exercises, week 1 is a [special_exercise], then [special_exercise], then [special_exercise], [special_exercise]",
            "It's like writing your name, once you learn how to spell it you can only spell it wrong",
            "People go to the Shaolin Temple, Shaolin Temple don't go to them",
            "We use [300-700] pounds of straight weight and [200-300] pounds of ['chains','band tension']"
        ],
        [
            "That's why we got over 140 world records",
            "And that's conjugate",
            "And that's how he beat [famous_lifter] at the meet",
        ],
    ]

    terms = {
        'westside_lifter': [
            'Chuck Vogelpohl',
            'Matt Dimel',
            'Dave Tate',
            'Smelly',
            'Kenny Patterson',
            'George Halbert',
            'AJ Roberts',
            'Laura Phelps',
            'Amy Weisberger',
            'Jason Coker',
            'Dave Hoff',
        ],
        'main_lift': ['squat', 'bench', 'deadlift'],
        'special_exercise': [
            'box squat',
            'good morning',
            'floor press',
            'board press',
            'reverse hyper',
            'sled drag',
            'illegal wide bench press',
        ],
        'famous_lifter': [
            'George Frenn',
            'Larry Pacifico',
            'Rickey Dale Crain',
            'Eddy Coan',
            'Donnie Thompson',
            'Don Reinhoudt',
            'Fred Hatfield',
            'Ernie Frantz',
        ],
        'muscle_group': [
            'lats',
            'triceps',
            'hips',
            'lower back',
            'hamstrings',
            'delts',
            'pecs',
            'abdominals',
        ], 
    }    
