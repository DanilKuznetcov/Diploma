# System for monitoring the dynamics of discussions in social network (VKontakte)

## Description
This project allows extract topics from social network and understand their daynamics. As initial data, needs: 
1. A key word, which will be searched for 
2. Set the analyzed time interval.

## Example
Analyzing publication by key-word "крипта" ("crypto"), the following result was obtained:
![image](https://github.com/DanilKuznetcov/Diploma/assets/49263683/6c914b39-fa39-4ede-bf6e-d2c35a26bc7c)

To analyze the dynamics, let's check how the interpretation for the 1st topic ("BTC") changes
![image](https://github.com/DanilKuznetcov/Diploma/assets/49263683/6a32ad9a-6f94-4ddd-8845-a216e8620c45)

You can compare it with chart of BTC in 2022 and find next correct trends:
![image](https://github.com/DanilKuznetcov/Diploma/assets/49263683/210f2889-0882-4269-9e42-6326f2588cd4)
1. The maximum popularity of the topic (the Frequency value is the maximum) corresponds to a sharp and maximum drop in May and June.
2. In February, the topic was characterized by the words "waves" and "rise in price", which corresponds to unstable growth on the chart for this period.
3. Analyst Mike McGlone and investor Tim Draper also appear in the interpretation of the topic for September and October, respectively. This is due to the fact that they gave a forecast for the growth of btc in these periods.

## Usage
The whole system is divided into three parts for the convenience of modification for specific topics (keywords).

### 1. Getting data
For this part you need create "1. Getting data/constants.py" file with you API keys, example:


    #VK API constants
    ACCESS_TOKEN = *
    API_URL = 'https://api.vk.com/method'
    V = '5.91'

After that, please change the main.a py file for your keyword and time frames
You will get result in csv file with next name - "{topic}_{start}-{end}.csv".

### 2. Preprocessing
Specify name of file with data in "Get data" block. 
You can tune filter to your needs too.
You recevied results in "cleaned_data.csv". Example:
- Before - "Дорогие инвесторы и трейдеры, вот и наступил 2022 год. Желаю Вам всем в этом году больше успешных сделок. Зеленых портфелей. Вылечиться от FOMO."
- After - "дорогой инвестор трейдер наступать 2022 желать успешный сделка зеленый портфель вылечиваться fomo"


### 3. Analyzing
* For analyzing using BERT model with d-TF-IDF metric representaion.
* You can change default model by your need, as default set - "multilingual".
* Please be aware, for dynamic analyzing you need round timestamps to ~50 uniqe values for representenive results
* The more data, the better the quality will be. Therefore, I advise you not to revise the time period shorter than a month.


