# TOC Project 2019

A Facebook messenger bot based on a finite state machine

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
	* 使用button輸入星座獲得星座圖片

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
		
	* Input: button postback
		* Earth Signs (go to `starEarth`)
		* Water Signs (go to `starWater`)
		* Next page (go to `fortune2`)
		
當使用者在 `fortune2` 時，會出現按鈕，按下會抵達對應的state
* `fortune2`
	* On entering
		* Show: three buttons
		
	* Input: button postback
		* Fire Signs (go to `starFire`)
		* Air Signs (go to `starAir`)
		* Next page (go to `fortune1`)
		
當使用者在 `starEarth` 時，會出現按鈕，按下會抵達對應的state
*  `starEarth`
	* On entering
		* Show: three buttons
		
	* Input: button postback
		* Taurus (go to `answerTaurus')
		* Virgo (go to `answerVirgo`)
		* Capricon (go to `answerCapricorn`)

當使用者在 `starWater` 時，會出現按鈕，按下會抵達對應的state
*  `starWater`
	* On entering
		* Show: three buttons
		
	* Input: button postback
		* Cancer (go to `answerCancer')
		* Scorpio (go to `answerScorpio`)
		* Pisces (go to `answerPisces`)
		
當使用者在 `starEarth` 時，會出現按鈕，按下會抵達對應的state
*  `starFire`
	* On entering
		* Show: three buttons
		
	* Input: button postback
		* Aries (go to `answerAries')
		* Leo (go to `answerLeo`)
		* Sagittarius (go to `answerSagittarius`)

當使用者在 `starAir` 時，會出現按鈕，按下會抵達對應的state
*  `starAir`
	* On entering
		* Show: three buttons
		
	* Input: button postback
		* Aquarius (go to `answerAquarius')
		* Gemini (go to `answerGemini`)
		* Libra (go to `answerLibra`)
		
當使用者在 `answerTaurus`, `answerVirgo`, `answerCapricorn`, `answerCancer`, `answerScorpio`, `answerPisces`, `answerAries`, `answerLeo`, `answerSagittarius`, `answerAquarius`, `answerGemini`, `answerLibra` ，會利用爬蟲獲得今日運勢，並且回到 `start`
* `answerTaurus`, `answerVirgo`, `answerCapricorn`, `answerCancer`, `answerScorpio`, `answerPisces`, `answerAries`, `answerLeo`, `answerSagittarius`, `answerAquarius`, `answerGemini`, `answerLibra` 

	* On entering
		* Show: 今日運勢
			* 利用爬蟲獲得今日運勢
		* go_back(): 回到 `start`
	
	
	
Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"
When user press the buttons, `start` state is triggered to `advance` to another state, and when user input text message, it will stay at  `start` 

#### Watch my video

#### Search for star logo

## Reference
[TOC-Project-2017](https://github.com/Lee-W/TOC-Project-2017) ❤️ [@Lee-W](https://github.com/Lee-W)
