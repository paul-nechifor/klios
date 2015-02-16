from django import template

register = template.Library()


@register.inclusion_tag('cards/card_front.html')
def card_front(card):
    return {'card': card}


@register.inclusion_tag('cards/card_back.html')
def card_back(card):
    return {'card': card}


@register.inclusion_tag('cards/card_full_info.html')
def card_full_info(card_info):
    return {'card_info': card_info}
