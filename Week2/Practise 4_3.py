def lang_genoeg(lengte):
    if lengte >= 120:
        tekst = 'Je bent lang genoeg voor de attractie'
        return tekst
    else:
        tekst = 'Sorry, je bent te klein'
        return tekst

print(lang_genoeg(120))