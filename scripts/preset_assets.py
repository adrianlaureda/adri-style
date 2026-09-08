"""Derivados de color y carga tipográfica del catálogo canónico."""
from __future__ import annotations

import colorsys
import re
from urllib.parse import urlencode
from validate_contract import font_weights


def rgb(value):
    if value.startswith('#'):
        return tuple(int(value[i:i+2],16)/255 for i in (1,3,5))
    match = re.fullmatch(r'hsl\(([\d.]+) ([\d.]+)% ([\d.]+)%\)',value)
    if not match:
        raise ValueError(f'Color no soportado: {value}')
    h,s,l = map(float,match.groups())
    return colorsys.hls_to_rgb(h/360,l/100,s/100)


def luminance(color):
    values = (v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb(color))
    return sum(v*w for v,w in zip(values,(.2126,.7152,.0722)))


def contrast(a,b):
    x,y = sorted((luminance(a),luminance(b)))
    return (y+.05)/(x+.05)


def foreground(background):
    chosen = max(('#101014','#ffffff'),key=lambda color: contrast(color,background))
    return chosen if contrast(chosen,background) >= 4.5 else '#000000'


def readable_accent(accent,background):
    """Conserva el acento; mezcla solo su variante para texto hasta AA."""
    target = foreground(background)
    a,b = rgb(accent),rgb(target)
    for step in range(101):
        ratio = step/100
        color = '#' + ''.join(f'{round((x*(1-ratio)+y*ratio)*255):02x}' for x,y in zip(a,b))
        if contrast(color,background) >= 4.5:
            return color
    return target


def font_stylesheets(preset):
    if "local_stylesheet" in preset["fonts"]:
        return ["../" + preset["fonts"]["local_stylesheet"]]
    families = {}
    for role in ('display','body'):
        name = preset['fonts'][role]
        families.setdefault(name,set()).update(font_weights(preset['fonts'][f'weights_{role}']))
    urls = []
    for name,weights in families.items():
        if name in {'Satoshi','Switzer','Clash Display'}:
            urls.append('https://api.fontshare.com/v2/css?' + urlencode({'f[]':name.lower().replace(' ','-')+'@1','display':'swap'}))
        else:
            # Extremos y peso de lectura; evita pedir pesos estáticos inexistentes.
            chosen = sorted({min(weights),max(weights)} | ({400} if 400 in weights else set()))
            query = {'family':name+':wght@'+';'.join(map(str,chosen)), 'display':'swap'}
            urls.append('https://fonts.googleapis.com/css2?'+urlencode(query))
    return urls


def preview_tokens(preset):
    bg,accent = preset['color']['bg'],preset['color']['accent']
    return {'text':foreground(bg),'accent_ink':readable_accent(accent,bg),
            'on_accent':foreground(accent),
            'display_weight':max(font_weights(preset['fonts']['weights_display'])),
            'body_weight':min(font_weights(preset['fonts']['weights_body']),key=lambda w:abs(w-400))}
