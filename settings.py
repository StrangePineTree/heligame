SCREEN_WIDTH = 1680
SCREEN_HEIGHT = 920

MAX_THRUST = 15 #default is 30
GRAVITY = 1 # default is 1
SPEED_MULTIPLIER = 1.0
GAME_SPEED_MODIFIER = 1
TURN_SPEED = 1.0
OVERLAY = True
RUNTIME = False
ATTACK_COOLDOWN = 1.0
ATTACK_SPEED = 1

HELITYPE = "transport"
#future heli types: UFO, attack, scout/basic, transport
#UFO will fly just by using arrow keys, no gravity or rotation
#attack will have lock on missiles and machine guns
#transport will have machine gun that can aim in any direction
#basic will be lame probebly

PARALLAX_FACTOR = 10

LAYERS = {
    'sky':1,
    'background':2,
    'ground': 3,
    'trees':5,
    'mountains':6,
    'main':7,
    'menu':8
}
