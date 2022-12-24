from fsm import TocMachine


def create_machine():
    machine = TocMachine(
        states=["user","mainpage",
        "menu","catfish","porkribs","catfishegg","mincedpork","rice","eggandtofu",
        "promotion","discount",
        "order","asknum","record","orderfinish",
        "information","businesshours","phonenum","address"
        ],
        transitions=[
            {#mainpage
                "trigger": "advance",
                "source": "user",
                "dest": "mainpage",
                "conditions": "is_going_to_mainpage"
            },
            {#backmainpage
                "trigger": "advance",
                "source": ["menu", "promotion", "order","information"],
                "dest": "mainpage",
                "conditions": "is_going_to_backmainpage"
            },
            {#menu
                "trigger": "advance",
                "source": "mainpage",
                "dest": "menu",
                "conditions": "is_going_to_menu"
            },
            {#catfish
                "trigger": "advance",
                "source": "menu",
                "dest": "catfish",
                "conditions": "is_going_to_catfish"
            },
            {#porkribs
                "trigger": "advance",
                "source": "menu",
                "dest": "porkribs",
                "conditions": "is_going_to_porkribs"
            },
            {#catfishegg
                "trigger": "advance",
                "source": "menu",
                "dest": "catfishegg",
                "conditions": "is_going_to_catfishegg"
            },
            {#mincedpork
                "trigger": "advance",
                "source": "menu",
                "dest": "mincedpork",
                "conditions": "is_going_to_mincedpork"
            },
            {#rice
                "trigger": "advance",
                "source": "menu",
                "dest": "rice",
                "conditions": "is_going_to_rice"
            },
            {#eggandtofu
                "trigger": "advance",
                "source": "menu",
                "dest": "eggandtofu",
                "conditions": "is_going_to_eggandtofu"
            },
            {#backmenu
                "trigger": "advance",
                "source": ["catfish","porkribs","catfishegg","mincedpork", "rice","eggandtofu"],
                "dest": "menu",
                "conditions": "is_going_to_backmenu"
            },
            {#promotion
                "trigger": "advance",
                "source": "mainpage",
                "dest": "promotion",
                "conditions": "is_going_to_promotion"
            },
            {#discount
                "trigger": "advance",
                "source": "promotion",
                "dest": "discount",
                "conditions": "is_going_to_discount"
            },
             {#backpromotion
                "trigger": "advance",
                "source": "discount",
                "dest": "promotion",
                "conditions": "is_going_to_backpromotion"
            },
            {#order
                "trigger": "advance",
                "source": "mainpage",
                "dest": "order",
                "conditions": "is_going_to_order"
            },
            {#asknum
                "trigger": "advance",
                "source": "order",
                "dest": "asknum",
                "conditions": "is_going_to_asknum"
            },
            {#record
                "trigger": "advance",
                "source": "asknum",
                "dest": "record",
                "conditions": "is_going_to_record"
            },
            {#orderfinish
                "trigger": "advance",
                "source": "order",
                "dest": "orderfinish",
                "conditions": "is_going_to_orderfinish"
            },
            {#backorder
                "trigger": "advance",
                "source": ["record","orderfinish"],
                "dest": "order",
                "conditions": "is_going_to_backorder"
            },
            {#information
                "trigger": "advance",
                "source": "mainpage",
                "dest": "information",
                "conditions": "is_going_to_information"
            },
            {#businesshours
                "trigger": "advance",
                "source": "information",
                "dest": "businesshours",
                "conditions": "is_going_to_businesshours"
            },
            {#phonenum
                "trigger": "advance",
                "source": "information",
                "dest": "phonenum",
                "conditions": "is_going_to_phonenum"
            },
            {#address
                "trigger": "advance",
                "source": "information",
                "dest": "address",
                "conditions": "is_going_to_address"
            },
            {#backinformation
                "trigger": "advance",
                "source": ["businesshours","phonenum","address"],
                "dest": "information",
                "conditions": "is_going_to_backinformation"
            }
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    #machine.get_graph().draw('my_state_diagram.png', prog = 'dot')
    return machine