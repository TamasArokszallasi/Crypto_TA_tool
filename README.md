# Technical Analysis of Cryptocurrencies with using big data


## Project Description
On my way of learning data analytics with python, sql and data visualising tools, i am constantly looking for projects that can challange my skills and i do own interest in the topic itself as well. 
I met the cryptocurrencies firstly in 2017, and since then i am constanly following it and looking with childish curiosity on what would be the next great innovation that can be solved by the blockchain industry itself. 
Furthermore, i do graduated as an economist, and have an urge to do analysis whenever i can on whatever come across. I think that's enoguh for the short sotrytelling, let me introduce the question, methodology and answers that made this project to be done.

Used softwaires and programming languages:
- Python (libraries: requests, pandas, concurrent.futures, datetime, os, TA-lib)
- Alteryx
- PowerBI
- Excel


**##Hypothesis 1**
Currently one of the hottest topic in cryptocurrency trading is looking at the japaneese candlestick charts to find some patterns and indicator signals that can predict the next move.
Do Japaneese candlestick pattern appearance can signal a price movment, and if yes, in a precision that it could be worth to follow it?

**##Hypothesis 2**
As i mentioned previously, i am looking over this industry weekly, sometimes daily, it depends on my business. But, what i do recognized is that cryptocurrency pairs against the USD are tend to move simoultaneously in the same direction. 
now at this point my hypothesises may extend into 2 or 3 hypothesis. I am wondering, which pair follows which movement? How to capture a movement? 

**##Hypothesis 3**
There are other variables that can influence the price movements, variables that are fundamental economic variables. How to catch em all? 


**##Hypothesis 4**
I am looking the pairs against the USDT, or other stablecoin, however these stablecoins are usually linked to other currency, more likely the USD. Is that issue can have any effect on the prices?


Okay, so in general economics, when we are using a variable to analyse for example the fxrate of a currency, we must reason it why we are using that variable. We must cite the one who have previously used this variable and tested, basically created it.
What would happen if we can create a variable which currently does not have any literature to use, is that makes the whole thing untrustful?

**Methodology briefly:**
I'm going to collect data with API, then by using python, the code will go through the data and looks for specific candlestick patterns. Then it tests if after the pattern appear, on which day was the pattern indication was true, and if it was true, what percentage was the movement. Then this output will be put into a BI tool to further analyse and gain insights.


**Methodology in details**

1. Obtaining the data

The data collection is the most crucial step, it have to be accurate, with the least missing value possible, and of course from a source which is reliable.
Since i am doing an analytics on cryptocurrencies, i figured out that the best option would be to collect data from the Binance website by using their free API, which is a genius thing, and so thankfull that i found that pretty quickly.

I defined 10 most popular cryptocurrencies by market cap, according to [coinmarketcap.com ](https://coinmarketcap.com/).  (stablecoins excluded)
**Pairs:**
Bitcoin (BTC): $1.85 trillion
Ethereum (ETH): $401.36 billion
XRP (XRP): $120.22 billion
BNB (BNB): $100.72 billion
Solana (SOL): $92.72 billion
Dogecoin (DOGE): $46.69 billion
Cardano (ADA): $29.79 billion
TRON (TRX): $21.96 billion
Avalanche (AVAX) $16.04 billion
Toncoin (TON): $14.13 billion
And for the sake of joy, i've added two of my favourite cryptocurrencies as well:
NEO (NEO): $1.0 billion
Chiliz (CHZ): $808.08 million

Generally, when doing technical analysis, it said that the more frequent the period observed, the least precises are the indicators and patterns.
I decided to do the analytics on the time periods of:
1Day (1D)
4Hours (4H)
1Hours (1H)
30Minutes (30M)
15Minutes (15M)
5Minutes (5M) 

The period i am planning to observe is 6 consecutive years (2019.01.01 - 2025.01.01 ) 

The patterns i am going too look for are:
hammer  
shooting star  
bullish engulfing  
bearish engulfing  
evening star  
morning star  
bullish harami  
bearish harami  
three black crows  
three white soldiers  
gravestone doji  
dragonfly doji  
bullish long legged doji  
bearish long legged doji  
hanging man  
inverted hammer  
piercing line  
dark cloud cover

There is no other input needed at this point.
With the file "Data extraction tool optimized.py" i run an optimized data collection tool, which gets all the data from the Binance API with the given period for all the pairs. I go one by one with each periods i mentioned above, and got all the csv files with raw data -each csv file cointains one period, but all pairs-. (see uploaded)
Then, another script going to run which is: "Ta_data_analytics_from_a_CSV" , this goes one by one through each of the csv files, and create another csv file with the completed analytics.
The output csv file will contain columns: 'Date', 'Pair', 'Pattern', 'Signal', 'Outcome', 'Percentage Movement'

Now at this point i have the following:
6 csv files, which only containes the 'Date', 'Pair', 'Open', 'Lowest, 'Highest', 'Close' columns. Approximately 10.5 million rows.
6 csv files, which is the analytics outcome, it cointains the following columns: 'Date', 'Pair', 'Pattern', 'Signal', 'Outcome', 'Percentage Movement'

At this point we must go to the next point, "Scrub".

2. Data cleaning and validation
So to go to the analytics, we have to concatenate all the analyzed csv files into one single files, to make it easier to navigate between periods later when analysing.
So i used Alteryx to easily combine all the files. (See the alteryx board here: [ Alteryx_Output_setup.png
](https://github.com/TamasArokszallasi/Crypto_TA_tool/blob/e9af88f0858801dbcc65b33ec9e1fde6a91498be/Alteryx_Output_setup.png) ) To be honest, this was the first time i am using Alteryx. I just literally fell in love with that. Amazing how easily it manages huge files, and the easiness of use is like magic. Firstly, i used jupyter notebook to combine these huge excel files, but later on i decided to go give a try to Alterix.

##Data Cleaning.

It appear that sometimes the model could not decide on which candlestick to choose, so it add both. This cause a bit of a uncertainity and i wanted to get rid of that, so i removed all the duplicated values with using Alteryx. 
So duplicate combinations of three columns: 'Date', 'Pair', 'Pattern'

3. Analyzing data & results

The most important, and doubtlessly the most exciting part just came. 
Now i put all the cleaned csv file to my faviourite visulising tool, PowerBI.

At this point i would kindly ask the reader to open each time the link (which is a picture uploaded to github) where he/she can observe the visualisation i am describing. Thank you! :)

First outlook of the data: https://github.com/TamasArokszallasi/Crypto_TA_tool/blob/83f021e6b0545bcbba37c77e55179c6aa45fb430/Total_basic_analytics.png
In this graph, we can see that the total outcome distribution of true and false was 73.05% True and 26.95% False. This means that almos 3/4 times the outcome prediction of a candlestick proven true, which is AMAZING, even unbeliveable. The rest two table shows that Bullish/Bearish signal distribution is almost equal, and by far, the leader in terms of appearance is the Long Legged Doji candlesticks patterns, both bullish/bearish.
I went through all the periods, and the worst performing was the 5minute where the false outcome were 27% and the best was the 1d period with 25%. Not a huge difference at all.

In this visualisation: https://github.com/TamasArokszallasi/Crypto_TA_tool/blob/4c7c2d11909034d62393a4eba9e5c0b4580613f4/T_F_distribution_per_pattern.png
We can see how the True and False outcomes distribute between the different pattern. There is no huge performance difference them. So in almost 75% in each pattern the outcome is true, the rest is false.

I have introduced the main analytic outcomes, the further investigation will take place later, when the times enables me to do so.

**4. Future**

The next step is to implement few indicators that are widely used, such as EMA, SMA, Stochastic RSI, Boillinger Band, Ichimoku Cloud or anything that relates, and do the analytical part for that as well. Those indicators are great to spot resistance or support lines in the prices. 

+1 future can be creating a trading bot which can signal me live if a pattern appear on a chart and i can act upon that.
+1 The network centrality analysis must taken place soon as well, here at my github most likely.

Thank you for reading it! :)




