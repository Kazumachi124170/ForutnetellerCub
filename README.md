# FortunetellerCup

A Facebook messenger bot based on a finite state machine
It can tell you your daily horoscope by crawling web

## Setup

#### Install Dependency
```sh
pip3 install -r requirements.txt
```
#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 4999
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./fsm.png)

## Usage
### 主要功能
* Tell my fortune
	* 使用button輸入星座獲得當日星座運勢
	* 爬蟲，利用BottleSoup分析網頁
* Watch my video
	* 使用button開啟影片連結
* Search for star logo
	* 使用button輸入星座獲得星座圖像

### 狀態介紹
初始狀態: `start`

當使用者在 `start` 時，輸入text message會讓state維持在 `start` 並且出現按鈕，按下按鈕則會離開 `start` 抵達對應的state
* `start`
	* On entering
		* Show: three buttons

	* Input: any text message
		* Show: three buttons

	* Input: button postback
		* Tell my fortune (go to `fortune1`)
		* Watch my video (go to `youtube`)
		* Search for star logo (go to `logo1`)
		
#### Tell my fortune
當使用者在 `fortune1` 時，會出現按鈕，按下會抵達對應的state
* `fortune1`
	* On entering
		* Show: three buttons
			* Earth Signs (go to `starEarth`)
			* Water Signs (go to `starWater`)
			* Next page (go to `fortune2`)
		
當使用者在 `fortune2` 時，會出現按鈕，按下會抵達對應的state
* `fortune2`
	* On entering
		* Show: three buttons
			* Fire Signs (go to `starFire`)
			* Air Signs (go to `starAir`)
			* Next page (go to `fortune1`)
		
當使用者在 `starEarth` 時，會出現按鈕，按下會抵達對應的state
*  `starEarth`
	* On entering
		* Show: three buttons
			* Taurus (go to `answerTaurus')
			* Virgo (go to `answerVirgo`)
			* Capricon (go to `answerCapricorn`)

當使用者在 `starWater` 時，會出現按鈕，按下會抵達對應的state
*  `starWater`
	* On entering
		* Show: three buttons
			* Cancer (go to `answerCancer')
			* Scorpio (go to `answerScorpio`)
			* Pisces (go to `answerPisces`)
		
當使用者在 `starEarth` 時，會出現按鈕，按下會抵達對應的state
*  `starFire`
	* On entering
		* Show: three buttons
			* Aries (go to `answerAries')
			* Leo (go to `answerLeo`)
			* Sagittarius (go to `answerSagittarius`)

當使用者在 `starAir` 時，會出現按鈕，按下會抵達對應的state
*  `starAir`
	* On entering
		* Show: three buttons
			* Aquarius (go to `answerAquarius')
			* Gemini (go to `answerGemini`)
			* Libra (go to `answerLibra`)
		
當使用者在 `answerTaurus`, `answerVirgo`, `answerCapricorn`, `answerCancer`, `answerScorpio`, `answerPisces`, `answerAries`, `answerLeo`, `answerSagittarius`, `answerAquarius`, `answerGemini`, `answerLibra` ，會利用爬蟲獲得今日運勢，並且回到 `start`
* `answerTaurus`, `answerVirgo`, `answerCapricorn`, `answerCancer`, `answerScorpio`, `answerPisces`, `answerAries`, `answerLeo`, `answerSagittarius`, `answerAquarius`, `answerGemini`, `answerLibra` 

	* On entering
		* Show: 今日運勢 (利用爬蟲獲得今日運勢)
		* go_back(): 回到 `start`

#### Watch my video
當使用者在 `video` 時，會出現按鈕，按下會跳出網站，或是抵達對應的state
* `video`
	* On entering
		* Show: three buttons
			* My film (go to happy tree friends youtube link)
			* MAMA (go to 皇阿瑪的后宮生活 fan page)
			* go back (go to `start`)

#### Search for star logo
當使用者在 `logo1` 時，會出現按鈕，按下會抵達對應的state
* `logo1`
	* On entering
		* Show: three buttons
			* Earth Signs (go to `logoEarth`)
			* Water Signs (go to `logoWater`)
			* Next page (go to `logo2`)
		
當使用者在 `logo2` 時，會出現按鈕，按下會抵達對應的state
* `logo2`
	* On entering
		* Show: three buttons
			* Fire Signs (go to `logoFire`)
			* Air Signs (go to `logoAir`)
			* Next page (go to `logo1`)
		
當使用者在 `logoEarth` 時，會出現按鈕，按下會抵達對應的state
*  `logoEarth`
	* On entering
		* Show: three buttons
			* Taurus (go to `logoTaurus')
			* Virgo (go to `logoVirgo`)
			* Capricon (go to `answerCapricorn`)

當使用者在 `logoWater` 時，會出現按鈕，按下會抵達對應的state
*  `logoWater`
	* On entering
		* Show: three buttons
			* Cancer (go to `logoCancer')
			* Scorpio (go to `logoScorpio`)
			* Pisces (go to `logoPisces`)
		
當使用者在 `logoEarth` 時，會出現按鈕，按下會抵達對應的state
*  `logoFire`
	* On entering
		* Show: three buttons
			* Aries (go to `logoAries')
			* Leo (go to `logoLeo`)
			* Sagittarius (go to `logoSagittarius`)

當使用者在 `logoAir` 時，會出現按鈕，按下會抵達對應的state
*  `logoAir`
	* On entering
		* Show: three buttons
			* Aquarius (go to `logoAquarius`)
			* Gemini (go to `logoGemini`)
			* Libra (go to `logoLibra`)

當使用者在 `logoTaurus`, `logoVirgo`, `logoCapricorn`, `logoCancer`, `logoScorpio`, `logoPisces`, `logoAries`, `logoLeo`, `logoSagittarius`, `logoAquarius`, `logoGemini`, `logoLibra` ，會出現星座符號，並且回到 `start`
* `logoTaurus`, `logoVirgo`, `logoCapricorn`, `logoCancer`, `logoScorpio`, `logoPisces`, `logoAries`, `logoLeo`, `logoSagittarius`, `logoAquarius`, `logoGemini`, `logoLibra` 

	* On entering
		* Show: image
		* go_back(): 回到 `start`
