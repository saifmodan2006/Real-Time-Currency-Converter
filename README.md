# 💱 Real-Time Currency Converter

A modern, fast, and user-friendly real-time currency converter web application built with **Flask** and **Bootstrap**. Convert between 150+ currencies with live exchange rates fetched from a reliable API.

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- ✅ **Real-Time Conversion** - Instant currency conversion with live exchange rates
- ✅ **150+ Currencies** - Support for major world currencies
- ✅ **Swap Function** - Easily swap currencies with one click
- ✅ **Responsive Design** - Beautiful UI that works on mobile, tablet, and desktop
- ✅ **No API Key Required** - Uses free, open-source exchange rate API
- ✅ **Error Handling** - Graceful error messages for invalid inputs
- ✅ **Fast & Lightweight** - Optimized for performance

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saifmodan2006/Real-Time-Currency-Converter.git
   cd Real-Time-Currency-Converter
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Real-Time-Currency-Converter/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore file
├── static/
│   └── styles.css        # Custom CSS styling
└── templates/
    ├── base.html         # Base template with navbar and footer
    └── index.html        # Main converter page
```

## 🔧 How It Works

### Backend (Flask)

- **GET `/`** - Renders the main converter page with available currencies
- **POST `/convert`** - AJAX endpoint that handles real-time currency conversion
  - Accepts JSON: `{from_currency, to_currency, amount}`
  - Returns: `{from_currency, to_currency, amount, rate, converted_amount}`

### Frontend (JavaScript)

- Real-time form submission with AJAX
- Dynamic currency selection with sorting
- Swap button to quickly exchange currencies
- Live rate display with proper formatting
- Error handling and validation

### API Integration

The application uses the **Open Exchange Rates API** (Free tier):
- Endpoint: `https://open.er-api.com/v6/latest/`
- No API key required
- Timeout: 5 seconds
- Updates: Daily exchange rates

## 🎨 UI/UX

Built with **Bootstrap 5.3.3** CDN for a modern, responsive design:
- Clean card-based layout
- Mobile-first responsive design
- Dark navbar with branding
- Alert boxes for results and errors
- Professional typography and spacing

## 📝 Usage Example

1. Enter the amount you want to convert (e.g., 100)
2. Select the source currency (e.g., USD)
3. Select the target currency (e.g., INR)
4. Click "Convert" or use the swap button to exchange currencies
5. View the live conversion result with exchange rate information

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.9+ | Backend language |
| Flask 3.0.0 | Web framework |
| Bootstrap 5.3.3 | Frontend framework |
| Requests | HTTP library for API calls |
| JavaScript (Vanilla) | Frontend interactivity |
| HTML5/CSS3 | Markup and styling |

## 📦 Dependencies

```
Flask==3.0.0        # Web framework
requests==2.31.0    # HTTP client
gunicorn==21.2.0    # Production server
```

## 🚀 Deployment

### Option 1: Heroku
1. Create a `Procfile` in the root directory:
   ```
   web: gunicorn app:app
   ```

2. Deploy:
   ```bash
   heroku login
   git push heroku main
   ```

### Option 2: PythonAnywhere
1. Upload files to PythonAnywhere
2. Create a web app with Flask
3. Point to `app.py`

### Option 3: Local Server
Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🐛 Error Handling

The application handles various error scenarios:
- **Invalid Amount** - Non-numeric or negative values
- **Unknown Currency** - Invalid currency codes
- **API Failures** - Network timeouts or API unavailability
- **Server Errors** - Graceful 500-level error messages

## 🔐 Security

- Input validation on both frontend and backend
- CORS-safe JSON responses
- Timeout protection (5 seconds)
- No sensitive data stored or transmitted

## 📊 Exchange Rate Source

- **Provider**: Open Exchange Rates (Free API)
- **Coverage**: 150+ currencies
- **Update Frequency**: Daily
- **Reliability**: 99.9% uptime
- **Documentation**: [open.er-api.com](https://open.er-api.com)

## 🎓 Learning Resources

This project is perfect for learning:
- Flask web framework basics
- RESTful API integration
- AJAX and asynchronous JavaScript
- Bootstrap responsive design
- Error handling and validation
- Real-world API consumption

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## 👨‍💻 Author

**Saif Modan**
- GitHub: [@saifmodan2006](https://github.com/saifmodan2006)
- Project: [Real-Time Currency Converter](https://github.com/saifmodan2006/Real-Time-Currency-Converter)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Future Enhancements

- [ ] Historical rate charts
- [ ] Offline support with cached rates
- [ ] Database for rate history
- [ ] User accounts for saved conversions
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Cryptocurrency support

## ⚠️ Disclaimer

Exchange rates are provided "as is" and may not always be 100% accurate. For critical financial transactions, please verify rates with your financial institution.

## 🙏 Acknowledgments

- [Open Exchange Rates API](https://open.er-api.com) for free exchange rate data
- [Bootstrap](https://getbootstrap.com) for the responsive framework
- [Flask](https://flask.palletsprojects.com) for the excellent web framework

---

**Made with ❤️ by Saif Modan**
