from transitions.extensions import GraphMachine
#import urllib2
import requests
from bs4 import BeautifulSoup
from utils import send_text_message
from utils import send_button_message
from utils import send_img_message
from utils import send_imgbutton_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        #self.to_start(event)

    def is_going_to_start(self, event):
        if event.get('message'):
            if event['message'].get('text'):
                text = event['message']['text']
                return True
        return False

    def is_going_to_startbut(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'start'
        return False

    def is_going_to_youtube(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'youtube'
        return False

    def is_going_to_fortune1(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'fortune1'
        return False

    def is_going_to_fortune2(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'fortune2'
        return False

    def is_going_to_starEarth(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'earth'
        return False

    def is_going_to_starWater(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'water'
        return False

    def is_going_to_starFire(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'fire'
        return False

    def is_going_to_starAir(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air'
        return False

    def is_going_to_answerAries(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'aries'
        return False

    def is_going_to_answerLeo(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'leo'
        return False

    def is_going_to_answerSagittarius(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'sagittarius'
        return False

    def is_going_to_answerAquarius(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'aquarius'
        return False

    def is_going_to_answerGemini(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'gemini'
        return False

    def is_going_to_answerLibra(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'libra'
        return False

    def is_going_to_answerTaurus(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'taurus'
        return False

    def is_going_to_answerVirgo(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'virgo'
        return False

    def is_going_to_answerCapricorn(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'capricorn'
        return False

    def is_going_to_answerCancer(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'cancer'
        return False

    def is_going_to_answerScorpio(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'scorpio'
        return False

    def is_going_to_answerPisces(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'pisces'
        return False

    def is_going_to_logo1(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'logo1'
        return False

    def is_going_to_logo2(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'logo2'
        return False

    def is_going_to_back(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'back'
        return False



    def on_enter_start(self, event):
        print("I'm entering start")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Tell my fortune!',
            'payload':'fortune1'
        },{
            'type':'postback',
            'title':'Watch my video!',
            'payload':'youtube'
            
        },{
            'type':'postback',
            'title':'Search for star logo!',
            'payload':'logo1'
        }]
        text = "Hi, I am a fortune teller!\nHow may I help you?"
        #responese = send_text_message(sender_id, "I'm entering state1")
        responese = send_button_message(sender_id, text, buttons)

    def on_enter_youtube(self, event):
        print("I'm entering youtube")
        sender_id = event['sender']['id']
        buttons = [{
            'type': 'web_url',
            'url': 'https://www.youtube.com/results?search_query=happy+tree+friends',
            'title': 'My film',
            'webview_height_ratio': 'full'

        },{
            'type': 'web_url',
            'url': 'https://www.facebook.com/fumeancats/?__tn__=kC-R&eid=ARCXNf6Dy7TtNr2EeIFMe7ae8WL1wDg5Y6tbXVy41rAAyxsKj1HInkVqZE5tS1ISI-4RNv7pgbJqFbdP&hc_ref=ARQfVb0cpautnvSiTIr8v9M_2uNIdzZfdjwXGG8_927ldBgwK6-k78MuopPGYINQAD4&fref=nf&__xts__%5B0%5D=68.ARDtbRW0ieCKFZDP5nsYWY1qAlsgpDQOoLHAz8KpQwZkxdu8KTdDw6vUv1TGYJtQRg9sFqqHPkorAtBhDBGZeY2nLY-SB1OYH5OURIFufl5DGerAHJ9F5FuCUntbw9uFsPE13x2LlG63bQtDGzi9-9Q8st4q_oss7ENwhbc8-EguQe-vhy8KZPi54GwsInNWdOyRTpQTByKqkR9RSkMZqVgC3VQTDeE1ROoBvfvauyI0ai87QVO_7GXuosHGbzm4yfN8YCQ2qrkFC6DDkUCuyWAgMGPPzMMM5tqPggxRMCIGeFIXM_gqiyQGVW-JKKXLbcJs9gQApUmNyouf0m0HPrpqoUVpxiEn7Y0lcoCbCL6iNbMvqFUNxeI',
            'title': 'MAMA',
            'webview_height_ratio': 'full'
        },{
            'type':'postback',
            'title':'go back',
            'payload':'start'
        }]
        responese = send_imgbutton_message(sender_id, "Which video would you like to watch <3 ?", buttons)
        
    def on_enter_fortune1(self, event):
        print("I'm entering fortune1")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Eatrh Signs',
            'payload':'earth'
        },{
            'type':'postback',
            'title':'Water Signs',
            'payload':'water'
            
        },{
            'type':'postback',
            'title':'Next page',
            'payload':'fortune2'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_fortune2(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Fire Signs',
            'payload':'fire'
        },{
            'type':'postback',
            'title':'Air Signs',
            'payload':'air'
            
        },{
            'type':'postback',
            'title':'Fore page',
            'payload':'fortune1'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logo1(self, event):
        print("I'm entering logo1")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Eatrh Signs',
            'payload':'earth'
        },{
            'type':'postback',
            'title':'Water Signs',
            'payload':'water'
            
        },{
            'type':'postback',
            'title':'Next page',
            'payload':'logo2'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logo2(self, event):
        print("I'm entering logo2")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Air Signs',
            'payload':'air'
        },{
            'type':'postback',
            'title':'Fire Signs',
            'payload':'fire'
            
        },{
            'type':'postback',
            'title':'For page',
            'payload':'logo1'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_starEarth(self, event):
        print("I'm entering startEarth")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Taurus',
            'payload':'taurus'
        },{
            'type':'postback',
            'title':'Virgo',
            'payload':'virgo'
            
        },{
            'type':'postback',
            'title':'Capricorn',
            'payload':'capricorn'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_starWater(self, event):
        print("I'm entering starWater")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Cancer',
            'payload':'cancer'
        },{
            'type':'postback',
            'title':'Scorpio',
            'payload':'scorpio'
            
        },{
            'type':'postback',
            'title':'Pisces',
            'payload':'pisces'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_starFire(self, event):
        print("I'm entering starFire")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Aries',
            'payload':'aries'
        },{
            'type':'postback',
            'title':'Leo',
            'payload':'leo'
            
        },{
            'type':'postback',
            'title':'Sagittarius',
            'payload':'sagittarius'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_starAir(self, event):
        print("I'm entering starAir")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Aquarius',
            'payload':'aquarius'
        },{
            'type':'postback',
            'title':'Gemini',
            'payload':'gemini'
            
        },{
            'type':'postback',
            'title':'Libra',
            'payload':'libra'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_answerAries(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Aries')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerLeo(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Leo')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerSagittarius(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Sagittarius')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerAquarius(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Aquarius')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerGemini(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Gemini')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerLibra(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Libra')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerTaurus(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Taurus')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerVirgo(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Virgo')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerCapricorn(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Capricorn')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerCancer(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Cancer')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerScorpio(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Scorpio')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

    def on_enter_answerPisces(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        r = requests.get('https://www.daily-zodiac.com/mobile/zodiac/Pisces')
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
        for a in articles:
            print(a.text)
            send_text_message(sender_id, a.text)
        self.go_back(event)

        """
        print("I'm entering logo")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://www.logolynx.com/images/logolynx/b2/b2744f197590a495e095e6195714515b.jpeg")
        self.go_back(event)
        """

    def on_enter_logoEarth(self, event):
        print("I'm entering startEarth")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Taurus',
            'payload':'taurus'
        },{
            'type':'postback',
            'title':'Virgo',
            'payload':'virgo'
            
        },{
            'type':'postback',
            'title':'Capricorn',
            'payload':'capricorn'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logoWater(self, event):
        print("I'm entering starWater")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Cancer',
            'payload':'cancer'
        },{
            'type':'postback',
            'title':'Scorpio',
            'payload':'scorpio'
            
        },{
            'type':'postback',
            'title':'Pisces',
            'payload':'pisces'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logoFire(self, event):
        print("I'm entering starFire")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Aries',
            'payload':'aries'
        },{
            'type':'postback',
            'title':'Leo',
            'payload':'leo'
            
        },{
            'type':'postback',
            'title':'Sagittarius',
            'payload':'sagittarius'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logoAir(self, event):
        print("I'm entering starAir")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Aquarius',
            'payload':'aquarius'
        },{
            'type':'postback',
            'title':'Gemini',
            'payload':'gemini'
            
        },{
            'type':'postback',
            'title':'Libra',
            'payload':'libra'
        }]
        responese = send_button_message(sender_id, "What is your zodiac type?", buttons)

    def on_enter_logoAries(self, event):
        print("I'm entering logoAries")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/1e/1c/62/1e1c62695b8fc29745693296bf0581ab.jpg")
        self.go_back(event)

    def on_enter_logoLeo(self, event):
        print("I'm entering logoLeo")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://www.logolynx.com/images/logolynx/b2/b2744f197590a495e095e6195714515b.jpeg")
        self.go_back(event)

    def on_enter_logoSagittarius(self, event):
        print("I'm entering logoSagittarius")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/99/ff/a5/99ffa5b53e4bc0d78c6837d665c9103e.jpg")
        self.go_back(event)

    def on_enter_logoAquarius(self, event):
        print("I'm entering logoAquarius")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i0.wp.com/s-media-cache-ak0.pinimg.com/564x/d5/99/b3/d599b30f32ccbdb3f0e8ee4b44bb62e2.jpg?resize=223%2C223&ssl=1")
        self.go_back(event)

    def on_enter_logoGemini(self, event):
        print("I'm entering logoGemini")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRes-uFIQKyWnqPe-8WARECcWJahQ5ZWpY_qVGOF0jAw2tGgKpyVA")
        self.go_back(event)

    def on_enter_logoLibra(self, event):
        print("I'm entering logoLibra")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/9b/b7/df/9bb7df9f13cca270f09fd72fabd88215.jpg")
        self.go_back(event)
        
    def on_enter_logoTaurus(self, event):
        print("I'm entering logoTaurus")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/564x/ef/08/9f/ef089fc22c344e468996c982d60c5daa.jpg")
        self.go_back(event)

    def on_enter_logoVirgo(self, event):
        print("I'm entering logoVirgo")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/736x/54/d8/7d/54d87dbfc1a42813fd2ec32479f35839--zodiac-star-signs-my-zodiac-sign.jpg")
        self.go_back(event)

    def on_enter_logoCapricorn(self, event):
        print("I'm entering logoCapricorn")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/9d/ac/ac/9dacac84cb047652f18a19167ff1c61a.jpg")
        self.go_back(event)

    def on_enter_logoCancer(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/c9/eb/61/c9eb613d053d639930365ea111a0c76f.jpg")
        self.go_back(event)

    def on_enter_logoScorpio(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/236x/fa/6b/34/fa6b34f4bde5d910660418afe8c8bff3--scorpio-art-scorpio-horoscope.jpg")
        self.go_back(event)

    def on_enter_logoPisces(self, event):
        print("I'm entering fortune2")
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://i.pinimg.com/originals/f2/d2/97/f2d2978f0168ccc8d385961ec5bac0f2.jpg")
        self.go_back(event)

        """
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://www.logolynx.com/images/logolynx/b2/b2744f197590a495e095e6195714515b.jpeg")
        self.go_back(event)
        """

