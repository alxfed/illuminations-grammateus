# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from yaml import safe_load as yl
from grammateus import Grammateus
from illuminations import rest as il

location = '/home/alxfed/Documents/Fairytales/three/'


def main():
    recorder = Grammateus(location)
    kwargs = """  # this is a string in YAML format
      model:        accounts/fireworks/models/deepseek-v3-0324
      max_tokens:   32000
      n: 2
      stop_sequences:
        - STOP
        - "\nTitle"
      temperature:  0.5
      top_k:        10
      top_p:        0.5
      # thinking:     24576  # thinking tokens budget. 24576
    """

    instruction = 'I am Joseph Jacobs. I retell folk tales'

    text_to_continue = 'Once upon a time when pigs drank wine'

    machine_text = il.continuation(
        text=text_to_continue,
        instruction=instruction,
        recorder=recorder,
        **yl(kwargs)
    )

    return machine_text


if __name__ == "__main__":
    result = main()
    ...
