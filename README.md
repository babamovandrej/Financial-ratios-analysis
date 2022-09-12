# Ratio_Analysis_Tool
 
 ## Ratio Analysis represents a package that can be used for financial statement analysis.
 
The package relies on already established ratios, commonly used in the financial world, to evaluate the performance of companies. The package captures aspects such as liquidity, solvency, profitablility, turnover, as well as earnings. In order to access the package functionalities, you will need to install the package. This can be done by running the code below:
 
```
pip install ratio-analysis==0.0.1

```
###After installing the package, you will need to import it in a python environment. After doing so, you can start divinng into company specifications. You can do this by implementing the following code snippet:

```
import ratio_analysis

company1 = ratio_analysis.Company_Analysis("company_name",year_of_analysis)

```
###or by using a more direct approach

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)

```
## Liquidity Analysis

In order to perform liquidity analysis, you must have information regarding the company's net income, total stockholders' equity, total current assets, total current liabilities, and total cash. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_liq_analysis = company1.liquidity_analysis(net_income,total_stockholders_equity,total_current_assets,total_current_liabilities,total_cash)

```
After doing so, you can perform the following ratios: return_on_equity(),current_ratio(),cash_ratio(), and net_working capital().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_liq_analysis = company1.liquidity_analysis(net_income,total_stockholders_equity,total_current_assets,total_current_liabilities,total_cash)
roe = company1_liq_analysis.return_on_equity()
print(roe)
```
## Solvency Analysis

In order to perform solvency analysis, you must have information regarding the company's total_liabilities, total stockholders' equity, and total assets. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_sol_analysis = company1.solvency_analysis(total_liabilities,total_stockholders_equity,total_assets)

```
After doing so, you can perform the following ratios: debt_to_equity(),debt_to_assets(), and financial_leverage_ratio().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_sol_analysis = company1.solvency_analysis(total_liabilities,total_stockholders_equity,total_assets)
d_t_e = company1_liq_analysis.debt_to_equity()
print(d_t_e)
```








