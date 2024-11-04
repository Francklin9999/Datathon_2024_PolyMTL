
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

Note that this app is integrated with AWS Bedrock services, you must configure the LLMs yourself as it can differ.
For LLMs functions, check the ai/ subdirectory

If you run this project locally you will have to configure your app with AWS CLI configuration steps can be fine here : https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-user.html

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
```<img width="863" alt="Screenshot 2024-11-04 112913" src="https://github.com/user-attachments/assets/72043f33-46d2-4ebd-9ebe-0f53604a5a0b">


```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run main.py
```

## Screenshots

<img width="949" alt="Screenshot 2024-11-04 112836" src="https://github.com/user-attachments/assets/88ba94<img width="878" alt="Screenshot 2024-11-04 113048" src="https://github.com/user-attachments/assets/6325e7d0-7867-4ec0-8d90-07e5f70418e3">
5b-1d06-4<img width="866" alt="Screenshot 2024-11-04 112855" src="https://github.com/user-attachments/assets<img width="853" alt="Screenshot 2024-11-04 113158" src="https://github.com/user-attachments/assets/c253e331-f3fb-48f5-a517-a975e2e28c6e"><img width="906" alt="Screenshot 2024-11-04 113255" src="https://github.com/user-attachments/assets/b64a2e90-ccd1-4400-9200-0b70b456fc5c">
<img width="906" alt="Screenshot 2024-11-04 113255" src="https://github.com/user-attachments/assets/72c47493-1d62-45c1-b9f6-7db41df4e562">

/ea6bb65c-b6e8-467b-83a8-36ccbb0f319e"><img width="865" alt="Screenshot 2024-11-04 113028" src="https://github.com/user-attachments/assets/cb12c79e-459a-4f79-9136-5e799e7b01bd"><img width="911" alt="Screenshot 2024-11-04 113232" src="https://github.com/user-attachments/assets/8aefcbd7-8503-4700-bebd-76d32adcf627">

<img width="872" alt="Screenshot 2024-11-04 113121" src="https://github.com/user-attachments/assets/d9b5bde9-e010-47e4-82e5-149b1812f26d">

0ce-b0cd-02180a2d9e9e"><img width="872" alt="Screenshot 2024-11-04 112935" src="https://github.com/user-attachme<img wi<img width="880" alt="Screenshot 2024-11-04 113107" src="https://github.com/user-attachments/assets/ac328cf7-b3ae-4a01-a1e7-5e6f284cbc9e">
dth="858" alt="Screenshot 2024-11-04 112952" src="https://github.com/user-attachments/assets/29ce22bc-7bef-49a4-b71d-47ca4c2216a5">
nts/assets/263471c5-294d-4bc8-bcf6-a53aaf6bf667">

