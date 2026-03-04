mapping = {'a':'а','c':'с','d':'ԁ','e':'е','g':'ց','h':'һ','i':'і','j':'ј','k':'κ','n':'ո','o':'о','p':'р','q':'ԛ','s':'ѕ','u':'ս','v':'ν','x':'х','y':'у','A':'А','B':'В','C':'С','D':'Ꭰ','E':'Е','F':'Ϝ','G':'Ԍ','I':'І','J':'Ј','K':'Κ','L':'Լ','M':'М','N':'Ν','O':'О','P':'Р','Q':'Ԛ','R':'Ꭱ','S':'Ѕ','T':'Τ','U':'Ս','V':'Ѵ','W':'Ѡ','X':'Х','Z':'Ζ'}
# text = input()
text = """The city woke slowly under gray rain.
Streetlights flickered like tired eyes.
Puddles mirrored broken neon signs.
A lone bicycle leaned against wet bricks.
Someone's forgotten umbrella spun in the wind.
Coffee steam rose from a cracked window.
Footsteps echoed without direction.
A stray cat watched everything silently.
Dawn arrived wearing someone else's coat.

Old radios still play songs nobody requests.
Vinyl scratches tell stories dust forgot.
Buttons fall off shirts no one mends.
Keys hang on hooks that lead nowhere.
Photos fade into the same soft yellow.
Clocks tick louder when rooms stay empty.
Letters wait inside drawers for replies.
Shadows remember faces that moved away.
Silence learns how to keep secrets well.

Trees grow sideways when wind never rests.
Roots grip stone more than soil.
Leaves fall before they finish turning red.
Branches scratch messages on passing clouds.
Birds build nests from broken plastic.
Rivers carry plastic bottles instead of fish.
Moss covers signs that once gave directions.
Fences lean like tired soldiers.
Nature reclaims what hurry abandoned.

Children invent games without winners.
Rules change every third heartbeat.
Cardboard becomes castle, spaceship, dragon.
Laughter bounces off walls that listen.
Sticks turn into swords, then wands, then nothing.
Mud becomes war paint, then evidence.
Sunsets are judged by color intensity.
Tomorrow feels far enough to promise anything.
Childhood ends the day someone explains time.

Night arrives without knocking twice.
Stars hide behind city glare politely.
Moths circle dying bulbs with devotion.
Thoughts grow louder when lights go out.
Dreams borrow shapes from yesterday's worries.
Sleep walks barefoot across cold floors.
Silence finally speaks in small whispers.
Morning waits behind the thinnest curtain.
Everything begins again without asking permission."""
output = ''.join(mapping.get(c,c) for c in text)
print(output)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(output)