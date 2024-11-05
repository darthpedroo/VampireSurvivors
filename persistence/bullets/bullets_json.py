import json
from persistence.bullets.bullets_dao import BulletDao
from business.entities.interfaces import IBullet

class BulletJson(BulletDao):
    
    def __init__(self, json_path:str):
        self.__json_path = json_path

    def get_bullets(self):
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data

    def save_bullets(self, bullets:[IBullet]):
        
        list_of_bullets_data = []
        
        try:
            for bullet in bullets:           
                json_data = bullet.create_bullet_json_data()
                list_of_bullets_data.append(json_data)
                #input("a")
            with open(self.__json_path , "w") as outfile:
                json.dump(list_of_bullets_data, outfile, indent=4)
        except UnboundLocalError:
            print("There are no Bullets to save !")

    def delete_bullets(self):
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(ex)


    