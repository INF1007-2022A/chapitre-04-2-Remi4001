#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
    return name.split("-")[0].capitalize()


def get_random_sentence(animals, adjectives, fruits):
    return (f"Aujourd’hui, j’ai vu un {random.choice(animals)} "
            f"s’emparer d’un panier {random.choice(adjectives)} "
            f"plein de {random.choice(fruits)}.")


def encrypt(text, shift):
    text = text.upper()
    shift %= 26
    encrypted_text = ""

    for char in text:
        if "A" <= char <= "Z":
            char = chr(ord(char) + shift)

            if char < "A":
                char = chr(ord(char) + 26)
            if char > "Z":
                char = chr(ord(char) - 26)

            encrypted_text += char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
    parrot = "jEaN-MARC"
    print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "mangue")
    print(get_random_sentence(animals, adjectives, fruits))

    print(encrypt("ABC", 1))
    print(encrypt("abc 123 XYZ", 3))
    print(decrypt("DEF 123 ABC", 3))
