# 🌊 Ocean Business Exhibitor Scraper  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange?logo=selenium)](https://www.selenium.dev/)  
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-brightgreen?logo=pandas)](https://pandas.pydata.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)  
[![Open Issues](https://img.shields.io/github/issues-raw/daemon403/web-scrapping)](https://github.com/daemon403/web-scrapping/issues)  

**A Python-based web scraper** that extracts, categorizes, and exports exhibitor data from the [Ocean Business](https://exhibitormanual.oceanbusiness.com/exhibitor-list-search/) website into a structured Excel file.  

---

## 📌 **Features**  

✅ **Automated Data Extraction**  
- Company names, stand locations, descriptions, products/services, and website URLs.  
- Handles pagination and dynamic content loading.  

✅ **Smart Categorization**  
- Classifies exhibitors into **10 industry sectors** (e.g., Marine Tech, Robotics, Sustainability).  
- Uses **keyword-based matching** with fallback to "Other" for ambiguous cases.  

✅ **Error-Resilient Design**  
- Gracefully handles missing data, network issues, and CAPTCHAs.  
- Logs errors without crashing.  

✅ **Excel Export**  
- Clean, formatted `.xlsx` output with:  
  - **Name** | **Stand** | **About** | **Products & Services** | **Website** | **Category**  

✅ **Easy Setup**  
- Automatic ChromeDriver installation via `webdriver-manager`.  
- Headless browser mode for server-friendly operation.  

---

## ⚙️ **Installation**  

### **Prerequisites**  
- Python 3.8+  
- Chrome or Edge browser installed  

### **Steps**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/daemon403/web-scrapping.git
   cd web-scrapping
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

---

## 🚀 **Usage**  

Run the scraper:  
```bash
python scraper.py
```  

### **Expected Output**  
1. **Console logs** show real-time progress and errors.  
2. **`ocean_business_exhibitors.xlsx`** is generated in the root directory.  

#### **Example Output**  
| Name          | Stand | Description                          | Products & Services       | Website          | Category          |  
|---------------|-------|--------------------------------------|---------------------------|------------------|-------------------|  
| 3DPRINTUK     | 19    | Leading 3D printing service...       | Composite Materials       | 3dprintuk.com    | Advanced Materials|  
| 4D Nav LLC    | K7    | Software for offshore energy...      | Survey, Navigation        | 4dnav.com        | Ocean Research    |  

---

## 🏷 **Category System**  
Exhibitors are classified into:  
1. **Energy Efficiency**  
2. **Alternative Fuels & Electrification**  
3. **Low-Carbon Economy**  
4. **Autonomous Shipping**  
5. **Advanced Materials & Sensors**  
6. **Marine & Subsea Technologies**  
7. **Ocean Research & Data Analytics**  
8. **Robotics & Automation**  
9. **Environmental Sustainability**  
10. **Other**  

*(Modify keywords in `scraper.py` to adjust classifications.)*  

---

## 🔧 **Troubleshooting**  

| Issue                  | Solution                                  |  
|------------------------|-------------------------------------------|  
| ChromeDriver errors    | Update Chrome or run `webdriver-manager update` |  
| Missing data in Excel  | Check `logs/error.log` for extraction issues |  
| CAPTCHAs/blocking      | Add `time.sleep()` delays between requests |  

---

## 📜 **License**  
MIT License. See [LICENSE](LICENSE) for details.  

---

## 🤝 **Contributing**  
1. Fork the repository.  
2. Create a branch (`git checkout -b feature/your-feature`).  
3. Submit a PR with clear documentation.  

**Bug reports** and **feature requests** are welcome via [GitHub Issues](https://github.com/daemon403/web-scrapping/issues).  

---

## 📌 **Disclaimer**  
This project is **for educational purposes only**. Always:  
- Check `robots.txt` before scraping.  
- Respect website terms of service.  
- Add delays to avoid overloading servers.  

*Not affiliated with Ocean Business or its partners.*  

---

**Happy Scraping!** 🚀

