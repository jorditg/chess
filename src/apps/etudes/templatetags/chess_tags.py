#!/usr/bin/env python

from django.template import Library

register = Library()


_aux_classes = {
        'A': 'w-question',
        'a': 'b-question',
        'e': 'wb-question',
    }


@register.assignment_tag
def get_piece(board, file, rank):
    piece = board[rank][file]
    if piece in 'KQRBNP':
        piece = dict(piece=piece, semantic_class='piece', board_class='w' + piece)
    elif piece in 'kqrbnp':
        piece = dict(piece=piece, semantic_class='piece', board_class='b' + piece)
    elif piece in 'Aae':
        piece = dict(piece=piece, semantic_class='aux-piece',
                     board_class=_aux_classes[piece])
    else:
        piece = None
    return piece


@register.filter
def split(string, separator):
    return string.split(separator)
