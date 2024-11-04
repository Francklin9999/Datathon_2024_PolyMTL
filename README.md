
# Datathon PolyMTL 2024 

This application tends to provide a easy and friendly interface for data anlyste to see, get an anlysis stock in term of making market predictions.


## Authors

- [Franck Fongang](https://github.com/Francklin9999)

- [Patrice Tohe](https://github.com/patricetohe)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY_FRED`
`API_KEY_ALPHAVANTAGE`
`API_KEY_FINANCIAL`
`API_KEY_FINNHUB`
`profile_name=equipe'number'`
`save_folder=/data`

API Keys are available for free here:

Fred :  https://fred.stlouisfed.org/docs/api/fred/
Alpha Vantage : https://www.alphavantage.co/
Financial : https://site.financialmodelingprep.com/
Finnhub : https://finnhub.io/
## Run Locally

Clone the project

```bash
  git clone https://github.com/Francklin9999/Datathon_2024_PolyMTL.git
```

Go to the project directory

```bash
  cd Datathon_2024_PolyMTL
```

Install dependencies

```bash
  You must compile the talib library locally.
  Doc to install can be find here:
  https://pypi.org/project/TA-Lib/
```

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run main.py
```

