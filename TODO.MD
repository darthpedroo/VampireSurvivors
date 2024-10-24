Todos los Stats de las armas van en 
GUNWITHBULLETS:
EJ:
    -COOLDOWN_TIME
    -DAMAGE
    -SPEED
    -ETC

ESTO ES PARA FACILITAR LA SUBIDA DE NIVELES.
PARA SUBIR DE NIVEL DESDE UN JSON, USAR 

SETTATTR
GETATTR

#Ejemplo de como subir de nivel...
def upgrade_next_level(self):
        setattr(self,"_GunWithBullets__base_shoot_cooldown", getattr(self,"_GunWithBullets__base_shoot_cooldown")-(getattr(self,"_GunWithBullets__base_shoot_cooldown"))*0.1)