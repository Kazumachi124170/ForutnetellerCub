from bottle import route, run, request, abort, static_file
from fsm import TocMachine


VERIFY_TOKEN = "kazuma"
machine = TocMachine(
    states=[
        'start',
        'fortune1',
        'fortune2',
        'starFire',
        'starAir',
        'starEarth',
        'starWater',
        'answerAries',
        'answerLeo',
        'answerSagittarius',
        'answerAquarius',
        'answerGemini',
        'answerLibra',
        'answerTaurus',
        'answerVirgo',
        'answerCapricorn',
        'answerCancer',
        'answerScorpio',
        'answerPisces',
        'logo1',
        'logo2',
        'logoAir',
        'logoFire',
        'logoEarth',
        'logoWater',
        'logoAries',
        'logoLeo',
        'logoSagittarius',
        'logoAquarius',
        'logoGemini',
        'logoLibra',
        'logoTaurus',
        'logoVirgo',
        'logoCapricorn',
        'logoCancer',
        'logoScorpio',
        'logoPisces',
        'youtube'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'fortune1',
            'conditions': 'is_going_to_fortune1'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'logo1',
            'conditions': 'is_going_to_logo1'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'youtube',
            'conditions': 'is_going_to_youtube'
        },
        {
            'trigger': 'advance',
            'source': 'youtube',
            'dest': 'start',
            'conditions': 'is_going_to_startbut'
        },
        {
            'trigger': 'advance',
            'source': 'logo1',
            'dest': 'logo2',
            'conditions': 'is_going_to_logo2'
        },
        {
            'trigger': 'advance',
            'source': 'logo2',
            'dest': 'logo1',
            'conditions': 'is_going_to_logo1'
        },
        {
            'trigger': 'advance',
            'source': 'logo1',
            'dest': 'logoEarth',
            'conditions': 'is_going_to_starEarth'
        },
        {
            'trigger': 'advance',
            'source': 'logo1',
            'dest': 'logoWater',
            'conditions': 'is_going_to_starWater'
        },
        {
            'trigger': 'advance',
            'source': 'logo2',
            'dest': 'logoAir',
            'conditions': 'is_going_to_starAir'
        },
        {
            'trigger': 'advance',
            'source': 'logo2',
            'dest': 'logoFire',
            'conditions': 'is_going_to_starFire'
        },
        {
            'trigger': 'advance',
            'source': 'logoFire',
            'dest': 'logoAries',
            'conditions': 'is_going_to_answerAries'
        },
        {
            'trigger': 'advance',
            'source': 'logoFire',
            'dest': 'logoLeo',
            'conditions': 'is_going_to_answerLeo'
        },
        {
            'trigger': 'advance',
            'source': 'logoFire',
            'dest': 'logoSagittarius',
            'conditions': 'is_going_to_answerSagittarius'
        },
        {
            'trigger': 'advance',
            'source': 'logoAir',
            'dest': 'logoAquarius',
            'conditions': 'is_going_to_answerAquarius'
        },
        {
            'trigger': 'advance',
            'source': 'logoAir',
            'dest': 'logoGemini',
            'conditions': 'is_going_to_answerGemini'
        },
        {
            'trigger': 'advance',
            'source': 'logoAir',
            'dest': 'logoLibra',
            'conditions': 'is_going_to_answerLibra'
        },
        {
            'trigger': 'advance',
            'source': 'logoEarth',
            'dest': 'logoVirgo',
            'conditions': 'is_going_to_answerVirgo'
        },
        {
            'trigger': 'advance',
            'source': 'logoEarth',
            'dest': 'logoTaurus',
            'conditions': 'is_going_to_answerTaurus'
        },
        {
            'trigger': 'advance',
            'source': 'logoEarth',
            'dest': 'logoCapricorn',
            'conditions': 'is_going_to_answerCapricorn'
        },
        {
            'trigger': 'advance',
            'source': 'logoWater',
            'dest': 'logoCancer',
            'conditions': 'is_going_to_answerCancer'
        },
        {
            'trigger': 'advance',
            'source': 'logoWater',
            'dest': 'logoScorpio',
            'conditions': 'is_going_to_answerScorpio'
        },
        {
            'trigger': 'advance',
            'source': 'logoWater',
            'dest': 'logoPisces',
            'conditions': 'is_going_to_answerPisces'
        },

        {
            'trigger': 'advance',
            'source': 'fortune1',
            'dest': 'fortune2',
            'conditions': 'is_going_to_fortune2'
        },
        {
            'trigger': 'advance',
            'source': 'fortune2',
            'dest': 'fortune1',
            'conditions': 'is_going_to_fortune1'
        },
        {
            'trigger': 'advance',
            'source': 'fortune1',
            'dest': 'starEarth',
            'conditions': 'is_going_to_starEarth'
        },
        {
            'trigger': 'advance',
            'source': 'fortune1',
            'dest': 'starWater',
            'conditions': 'is_going_to_starWater'
        },
        {
            'trigger': 'advance',
            'source': 'fortune2',
            'dest': 'starFire',
            'conditions': 'is_going_to_starFire'
        },
        {
            'trigger': 'advance',
            'source': 'fortune2',
            'dest': 'starAir',
            'conditions': 'is_going_to_starAir'
        },
        {
            'trigger': 'advance',
            'source': 'starFire',
            'dest': 'answerAries',
            'conditions': 'is_going_to_answerAries'
        },
        {
            'trigger': 'advance',
            'source': 'starFire',
            'dest': 'answerLeo',
            'conditions': 'is_going_to_answerLeo'
        },
        {
            'trigger': 'advance',
            'source': 'starFire',
            'dest': 'answerSagittarius',
            'conditions': 'is_going_to_answerSagittarius'
        },
        {
            'trigger': 'advance',
            'source': 'starAir',
            'dest': 'answerAquarius',
            'conditions': 'is_going_to_answerAquarius'
        },
        {
            'trigger': 'advance',
            'source': 'starAir',
            'dest': 'answerGemini',
            'conditions': 'is_going_to_answerGemini'
        },
        {
            'trigger': 'advance',
            'source': 'starAir',
            'dest': 'answerLibra',
            'conditions': 'is_going_to_answerLibra'
        },
        {
            'trigger': 'advance',
            'source': 'starEarth',
            'dest': 'answerVirgo',
            'conditions': 'is_going_to_answerVirgo'
        },
        {
            'trigger': 'advance',
            'source': 'starEarth',
            'dest': 'answerTaurus',
            'conditions': 'is_going_to_answerTaurus'
        },
        {
            'trigger': 'advance',
            'source': 'starEarth',
            'dest': 'answerCapricorn',
            'conditions': 'is_going_to_answerCapricorn'
        },
        {
            'trigger': 'advance',
            'source': 'starWater',
            'dest': 'answerCancer',
            'conditions': 'is_going_to_answerCancer'
        },
        {
            'trigger': 'advance',
            'source': 'starWater',
            'dest': 'answerScorpio',
            'conditions': 'is_going_to_answerScorpio'
        },
        {
            'trigger': 'advance',
            'source': 'starWater',
            'dest': 'answerPisces',
            'conditions': 'is_going_to_answerPisces'
        },
        {
            'trigger': 'go_back',
            'source': [
                'answerAries',
                'answerLeo',
                'answerSagittarius',
                'answerAquarius',
                'answerGemini',
                'answerLibra',
                'answerTaurus',
                'answerVirgo',
                'answerCapricorn',
                'answerCancer',
                'answerScorpio',
                'answerPisces',
                'logoAries',
                'logoLeo',
                'logoSagittarius',
                'logoAquarius',
                'logoGemini',
                'logoLibra',
                'logoTaurus',
                'logoVirgo',
                'logoCapricorn',
                'logoCancer',
                'logoScorpio',
                'logoPisces',
                'youtube'
            ],
            'dest': 'start'
        }
    ],
    initial='start',
    auto_transitions=True,
    show_conditions=True,
    ignore_invalid_triggers=False
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=4999, debug=True, reloader=True)
