from otree.api import *
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

age=[]
for i in range(15,60):
    age.append([i,str(i) +"歳"])


class Player(BasePlayer):
    offer = models.CurrencyField()
    budget = models.CurrencyField()
    a = models.CharField()
    offer = models.CurrencyField()
    budget = models.CurrencyField()
    name = models.CharField()
    age = models.IntegerField(
        label='あなたの年齢は？',
        choices=age
    )
    department = models.CharField(
        initial=None,
        choices=["文学","人間科","外国語","法",'経済学',"理学",'医学',"歯","薬","工","基礎工"],
        label='あなたの所属する学部、研究科は？',
    )
    #学年
    grade = models.CharField(
        initial=None,
        choices=[["B",'学部'],["M",'修士'],["D",'博士']],
        label='あなたの学年は？',
    )
    gender = models.StringField(
        choices=[['Male', '男性'], ['Female', '女性'], ['Other', 'その他']],
        label='あなたの性別は?',
    )
    # crt_bat = models.IntegerField(
    #     label='''
    #     A bat and a ball cost 22 dollars in total.
    #     The bat costs 20 dollars more than the ball.
    #     How many dollars does the ball cost?'''
    # )
    # crt_widget = models.IntegerField(
    #     label='''
    #     "If it takes 5 machines 5 minutes to make 5 widgets,
    #     how many minutes would it take 100 machines to make 100 widgets?"
    #     '''
    # )
    # あ = models.IntegerField(
    #     label='''
    #     In a lake, there is a patch of lily pads.
    #     Every day, the patch doubles in size.
    #     If it takes 48 days for the patch to cover the entire lake,
    #     how many days would it take for the patch to cover half of the lake?
    #     '''
    # )


# FUNCTIONS

# def fruit_choices(player):
#     import random
#     choices = ['apple', 'kiwi', 'mango']
#     random.shuffle(choices)
#     return choices

# def offer_max(player):
#     return player.budget

# def offer_error_message(player, value):
#     print('value is', value)
#     if value > player.budget:
#         return 'Cannot offer more than your remaining budget'

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','department','grade']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget',"あ"]


page_sequence = [Demographics]
#, CognitiveReflectionTest