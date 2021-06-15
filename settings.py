from os import environ


SESSION_CONFIGS = [
   {
       'name': 'MPL',
       'display_name': "MPL",
       'num_demo_participants': 1,
       'app_sequence': ['MPL'],
   },
   {
       'name': 'Instraction',
       'display_name': "Instraction",
       'num_demo_participants': 1,
       'app_sequence': ['Instraction'],
   },
   {
       'name': 'practice',
       'display_name': "practice",
       'num_demo_participants': 1,
       'app_sequence': ['practice'],
   },
   {
       'name': 'main_experiment',
       'display_name': "main_experiment",
       'num_demo_participants': 1,
       'app_sequence': ['survey','search','cardflip','payment_info'],
   },
   {
       'name': 'search',
       'display_name': "search",
       'num_demo_participants': 1,
       'app_sequence': ['search','payment_info'],
   },
   {
       'name': 'cardflip',
       'display_name': "cardflip",
       'num_demo_participants': 1,
       'app_sequence': ['cardflip'],
   },
    {
        'name':'survey',
        'display_name': "survey",
        "name":'survey',
        "app_sequence":['survey', 'payment_info'],
        "num_demo_participants":1,
    },
    ]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

###
import datetime
dt_now = datetime.datetime.now()
deploy_time=str(dt_now.year)+"/"+str(dt_now.month)+"/"+str(dt_now.day) +"/"+str(dt_now.hour)+":"+str(dt_now.minute)


ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '7167722945861'

INSTALLED_APPS = ['otree']
