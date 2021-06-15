from otree.api import *
import random



doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'search'
    players_per_group = None
    num_trials=1
    para=[1,100]
    search_cost=1
    num_rounds = 2
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #offer_accepted = models.BooleanField()
    result = models.CurrencyField(initial=0)
    search_num = models.IntegerField(initial=0)
    current_best_value = models.IntegerField(initial=0)
    current_value = models.IntegerField(initial=0)
    seaquence = models.LongStringField(initial='0')
    #search_finished = models.BooleanField(initial=False)
    #value_seaquence=[]
    pass


# Function
def make_random():
    para_a=Constants.para[0]
    para_b=Constants.para[1]
    tmp=random.randint(para_a,para_b+1)
    return int(tmp)


#def is_finished(player: Player):
#    return player.search_finished == True

def get_state(player: Player):
    return dict(
        current_best_value=player.current_best_value,
        current_value=player.current_value,
        search_num=player.search_num,
        total_cost=player.search_num*Constants.search_cost
    )

# PAGES
class Search(Page):

    #  html to サーバー
    @staticmethod
    def live_method(player: Player,data):
        if data["conti"]:
            player.search_num=player.search_num+1
            current_value=make_random()
            player.seaquence= player.seaquence+","+str(current_value)
            if current_value > player.current_best_value:
                player.current_best_value=current_value
            player.current_value=current_value 
            player.result=player.current_best_value-player.search_num*Constants.search_cost
            return {player.id_in_group : get_state(player)}
        else:
            return {player.id_in_group : get_state(player)}



class Results(Page):
    pass


page_sequence = [Search, Results]
