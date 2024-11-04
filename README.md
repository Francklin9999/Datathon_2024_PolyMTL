
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
```

```bash
  pip install -r requirements.txt
```
Start the server

```bash
  streamlit run main.py
```

## Screenshots
<img width="949" alt="Screenshot 2024-11-04 112836" src="https://github.com/user-attachments/assets/a3ce5be0-40b4-4ceb-a15c-6ee8fb03d977">
<img width="866" alt="Screenshot 2024-11-04 112855" src="https://github.com/user-attachments/assets/e1f59049-15a7-493f-904e-ac074824975d">
<img width="863" alt="Screenshot 2024-11-04 112913" src="https://github.com/user-attachments/assets/c9d8963a-03a1-4cb7-8ff7-3c54e9f0e184">
<img width="872" alt="Screenshot 2024-11-04 112935" src="https://github.com/user-attachments/assets/fac10151-b569-4207-b714-aac58d0e49da">
<img width="858" alt="Screenshot 2024-11-04 112952" src="https://github.com/user-attachments/assets/a76cac55-7262-4b90-a183-0ecb04d5fe7c">
<img width="865" alt="Screenshot 2024-11-04 113028" src="https://github.com/user-attachments/assets/01639775-4e34-48dd-976f-530b468f468c">
<img width="878" alt="Screenshot 2024-11-04 113048" src="https://github.com/user-attachments/assets/619b5cd9-51ca-46ac-a7f1-a534095f49a6">
<img width="880" alt="Screenshot 2024-11-04 113107" src="https://github.com/user-attachments/assets/d0ef9c62-26df-4194-8e72-58eda05788c4">
<img width="872" alt="Screenshot 2024-11-04 113121" src="https://github.com/user-attachments/assets/7cea70a8-fca3-4d9e-badb-8c43d1523533">
<img width="852" alt="Screenshot 2024-11-04 113140" src="https://github.com/user-attachments/assets/1fcd81f6-b7b2-4cd2-a748-5da13cf9cc8f">
<img width="853" alt="Screenshot 2024-11-04 113158" src="https://github.com/user-attachments/assets/3bbbe144-4952-46fe-b39a-b751c18bae0f">
<img width="911" alt="Screenshot 2024-11-04 113232" src="https://github.com/user-attachments/assets/47ee20c3-25cd-40f2-86b9-605a159c1b1c">
<img width="906" alt="Screenshot 2024-11-04 113255" src="https://github.com/user-attachments/assets/9d75f052-ff09-464d-9e76-e8314ddef109">


