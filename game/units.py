import random
import os
class Player(object):

    def __init__(self, email, password, name='Player'):
        self.email = email
        self.password = password
        self.name = name
        self.list_of_squads = []

    def add_new_squad(self, captain_tree, hierophant_tree, nation):
        self.list_of_squads.append(Squad(captain_tree, hierophant_tree, nation))


class Stash(object):
    def __init__(self):
        self.list_of_items = []
        self.list_of_equipment = []

    def add_to_items(self, item):
        self.list_of_items.append(item)

    def remove_from_items(self, item):
        self.list_of_items.remove(item)

    def add_to_equipment(self, item):
        self.list_of_equipment.append(item)

    def remove_from_equipment(self, item):
        self.list_of_equipment.remove(item)


class Squad(object):

    def __init__(self, captain_tree, hierophant_tree, nation):
        self.squad_name = 'Best Squad'
        self.roster = []
        self.squad_visibility = 'Public'
        self.squad_credits = 500
        self.captain = Captain(captain_tree)
        self.hierophant = Hierophant(hierophant_tree)
        self.battle_team = []
        self.nation = nation
        self.stash = Stash()

    def add_to_roster(self, solider):
        self.roster.append(solider)
        #print(self.roster)

    def remove_from_roster(self, soldier):
        self.roster.remove(soldier)

    def add_to_battle_team(self, soldier):
        self.battle_team.append(soldier)

    def remove_from_battle_team(self, soldier):
        self.battle_team.remove(soldier)


class BasicStats(object):

    def __init__(self, start=1, stop=10, modifiers=False, **kwargs):
        self.name = kwargs.get('name', "name" + str(random.randint(start, 999)))
        self.move = kwargs.get('move', random.randint(start, stop))
        self.fight = kwargs.get('fight', random.randint(start, stop))
        self.shoot = kwargs.get('shoot', random.randint(start, stop))
        self.armour = kwargs.get('armour', random.randint(start, stop))
        self.morale = kwargs.get('morale', random.randint(start, stop))
        self.health = kwargs.get('health', random.randint(start, stop))
        self.cost = kwargs.get('cost', 0)
        self.pic = self.random_pic('images/soldier_icons')
        path = os.path.dirname(os.path.realpath(__file__))
        img = 'images/plain_square.png'
        self.item_empty_slot = os.path.join(path, img)
        if modifiers:
            self.move_mod = kwargs.get('move_mod', 0)
            self.fight_mod = kwargs.get('fight_mod', 0)
            self.shoot_mod = kwargs.get('shoot_mod', 0)
            self.armour_mod = kwargs.get('armour_mod', 0)
            self.morale_mod = kwargs.get('morale_mod' ,0)
            self.health_mod = kwargs.get('health_mod', 0)


    def calc_cost(self, factor_min=1, factor_max=1):
        '''
        Calculate cost based on basic stats.
        '''
        factor = random.uniform(factor_min, factor_max)
        stat_sum = sum([i for i in self.__dict__.values() if isinstance(i, int)])
        return int(stat_sum * factor)

    def random_pic(self, path):
        p=os.path.dirname(os.path.realpath(__file__))
        imgpath = os.path.join(p, path)
        img = random.choice(os.listdir(imgpath))
        #print(img)
        return os.path.join(imgpath, img)

    def gen_random_equipment(self):
        eq = ['Bow', 'Sword', 'Gun', 'Feather', 'Pen']
        return random.choice(eq)


class Weapon(BasicStats):

    def __init__(self, start=1, stop=20, **kwargs):
        super(Weapon, self).__init__(start, stop, **kwargs)
        self.cost = kwargs.get('cost', self.calc_cost(0.8, 1.2))
        self.pic = self.random_pic('images/weapons')
        self.type = self.gen_random_equipment()


class Item(BasicStats):

    def __init__(self, start=1, stop=10, **kwargs):
        super(Item, self).__init__(start, stop, **kwargs)
        self.cost = kwargs.get('cost', self.calc_cost(0.8, 1.2))
        self.pic = self.random_pic('images/items')
        self.type = self.gen_random_equipment()


class Soldier(BasicStats):

    def __init__(self, start=1, stop=100, modifiers=True, **kwargs):
        super(Soldier, self).__init__(start, stop, modifiers, **kwargs)
        self.name = kwargs.get('name', "Unit" + str(random.randint(1,999)))
        self.cost = kwargs.get('cost', self.calc_cost(0.8, 1.2))
        self.weapons = [Weapon()]
        self.items = [Item() for i in range(2)]

class Captain(Soldier):

    def __init__(self, captain_tree, **kwargs):
        super(Captain, self).__init__(**kwargs)
        self.name = kwargs.get('name', "Captain")
        self.tree = captain_tree
        self.experience = random.randint(23,89)
        self.available_skills = []
        self.weapons = [Weapon() for i in range(random.choice([2,3,4]))]
        self.items = [Item() for i in range(4)]

class Hierophant(Soldier):

    def __init__(self, hierophant_tree, **kwargs):
        super(Hierophant, self).__init__(**kwargs)
        self.name = kwargs.get('name', "Hierophant")
        self.tree = hierophant_tree
        self.experience = random.randint(23,89)
        self.available_skills = []
        self.weapons = [Weapon() for i in range(1)]
        self.items = [Item() for i in range(3)]

class ItemEquipmentList(object):
    def __init__(self):
        self.item_list = self.gen_item_list()
        self.equipment_list = self.gen_weapon_list()

    def gen_item_list(self):
        return [Item() for i in range(40)]

    def gen_weapon_list(self):
        return [Weapon() for i in range(40)]

class OnlinePlayers(object):
    def __init__(self):
        self.list_of_players = [Player('email', str(i), 'Player'+str(i)) for i in range(33)]

if __name__ == '__name__':
    print(ItemEquipmentList().item_list[34].cost)
    print(OnlinePlayers().list_of_players[12].name)
    print(Weapon().__dict__)
    player = Player('em@em.com', 'pass')
    player.add_new_squad('Captree', 'HereTree', 'Slask')
    print(player.list_of_squads[0].captain.__dict__)
