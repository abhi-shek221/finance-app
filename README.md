# Finance App

## Description

This is a Streamlit-based web application that leverages Google Generative AI (Gemini) to analyze and provide insights on financial statements. The application allows users to upload financial data files (Balance Sheet, Profit & Loss Statement, and Cash Flow Statement) in CSV format and generates comprehensive AI-powered summaries, insights, and visualizations.

## Features

- **File Upload**: Support for uploading CSV files for different financial statements
- **AI Analysis**: Uses Google Gemini AI to generate detailed financial insights
- **Visualizations**: Interactive charts and data visualizations using Streamlit
- **Comprehensive Reports**: Provides asset-liability summaries, revenue analysis, profitability insights, and cash flow explanations
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface

## Installation

1. **Clone the repository**:

```bash
   git clone <repository-url>
   cd finance-app

```

2. **Install dependencies**:

```bash
   pip install -r requirements.txt

```

3. **Set up Google API Key**:
   - Obtain a Google AI API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the `API_KEY` variable in `app.py` with your API key

4. **Run the application**:

```bash
   streamlit run app.py

```

## Usage

1. **Start the Application**: Run the command above to launch the Streamlit app in your browser

2. **Upload Financial Data**:
   - Upload Balance Sheet CSV file
   - Upload Profit & Loss Statement CSV file
   - Upload Cash Flow Statement CSV file

3. **Generate Reports**: Click the "Generate Reports" button to process the data

4. **View Results**:
   - AI-generated summaries for each financial statement
   - Interactive data visualizations
   - Detailed insights and recommendations

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Google Generative AI (google-generativeai)

## Project Structure

```
finance-app/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── balance_sheet.csv              # Sample balance sheet data
├── profit_loss.csv                # Sample profit & loss data
├── cash_flow.csv                  # Sample cash flow data
├── Project Documentation/         # Project documentation files
│   ├── 1. Ideation Phase/
│   ├── 2. Requirement Analysis/
│   ├── 3. Project Design Phase/
│   ├── 4. Project Planning Phase/
│   ├── 5. Project Development Phase/
│   └── 6. Project Documentation/
└── README.md                      # This file
```

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Generative AI (Gemini 1.5 Flash)
- **Data Processing**: Pandas
- **Visualization**: Streamlit's built-in charting capabilities

## How It Works

1. **Data Upload**: Users upload CSV files containing financial data
2. **Data Processing**: Pandas reads and processes the CSV data
3. **AI Analysis**: Google Gemini AI analyzes the data using predefined prompts
4. **Report Generation**: AI generates natural language summaries and insights
5. **Visualization**: Streamlit creates interactive charts and displays results

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional financial advice. Always consult with qualified financial professionals for investment decisions.
