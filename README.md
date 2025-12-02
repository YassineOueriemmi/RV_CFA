# RV_CFAxAmplifyMe.py

A lightweight Python/Tkinter tool that calculates **long/short quantities** based on price inputs, base notional, and target net exposure.

This tool computes:

- Long & short **notionals**
- Long & short **quantities**
- Custom **net exposure** (0 → 500k)
- Relative-value position sizing between two assets

Designed for quick usage and training practice (AmplifyME, CFA, trading games, interview prep, etc.).

---

## Functionality

### **Inputs**
- Long ticker price  
- Short ticker price  
- Base notional  
- Target net exposure  

### **Calculations**
- Long Notional = Base Notional + (Net Exposure / 2)
- Short Notional = Base Notional - (Net Exposure / 2)

- Long Quantity = Long Notional / Price A
- Short Quantity = Short Notional / Price B

---
### **How to Run**

Requires **Python 3.8+** (Tkinter included by default).

```bash
python RV_CFAxAmplifyMe.py
