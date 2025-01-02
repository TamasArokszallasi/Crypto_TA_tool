# Technical Analysis of Cryptocurrencies using OSEMN Data Science Life Cycle


## Project Description
On my way of learning data analytics with python, sql and data visualising tools, i am constantly looking for projects that can challange my skills and i do own interest in the topic itself as well. 
I met the cryptocurrencies firstly in 2017, and since then i am constanly following it and looking with childish curiosity on what would be the next great innovation that can be solved by the blockchain industry itself. 
Furthermore, i do graduated as an economist, and have an urge to do analysis whenever i can on whatever come across. I think that's enoguh for the short sotrytelling, let me introduce the question, methodology and answers that made this project to be done.
Lastly, but not least, i am using the OSEMN methodology to go through the analysis.


**##Hypothesis 1**
Currently one of the hottest topic in cryptocurrency trading is looking at the japaneese candlestick charts to find some patterns and indicator signals that can predict the next move.
Do Japaneese candlestick pattern appearance can signal a price movment, and if yes, in a precision that it could be worth to follow it?

**##Hypothesis 2**
As i mentioned previously, i am looking over this industry weekly, sometimes daily, it depends on my business. But, what i do recognized is that cryptocurrency pairs against the USD are tend to move simoultaneously in the same direction. 
now at this point my hypothesises may extend into 2 or 3 hypothesis. I am wondering, which pair follows which movement? How to capture a movement? 

**##Hypothesis 3**
What other variables can be useful in terms of capturing the movements of the currencies? Central banks ?

Okay, so in general economics, when we are using a variable to analyse for example the fxrate of a currency, we must reason it why we are using that variable. We must cite the one who have previously used this variable and tested, basically created it.
What would happen if we can create a variable which currently does not have any literature to use, is that makes the whole thing untrustful?

**Methodology briefly:**
I'm going to collect data with API, then by using python, the code will go through the data and looks for specific candlestick patterns. Then it tests if after the pattern appear, on which day was the pattern indication was true, and if it was true, what percentage was the movement. Then this output will be put into a BI tool to further analyse and gain insights.


**Methodology in details**

1. Obtain
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

1Minutes (1M) This will only be used later in the network centrality analytics.

The period i am planning to observe is 7 consecutive years (2018.01.01 - 2025.01.01 ) 

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

There is no other input needed at this point. Now we can run the code, it goes through the period, collects pair data, then analyse them and validate if the outcome was true or false, then if true, on which period after the appearance it became true, and what percentage movement do happen.
The output csv file will contain columns: 'Date', 'Pair', 'Pattern', 'Signal', 'Outcome', 'Percentage Movement'



3. Scrub
4. Explore
5. Model
6. iNterpret


**##Scrub
