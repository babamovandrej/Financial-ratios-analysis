# Ratio_Analysis_Tool
 
 ## Ratio Analysis represents a package that can be used for financial statement analysis.
 
The package relies on already established ratios, commonly used in the financial world, to evaluate the performance of companies. The package captures aspects such as liquidity, solvency, profitablility, turnover, as well as earnings. In order to access the package functionalities, you will need to install the package. This can be done by running the code below:
 
```
pip install financial-ratio-analysis

```
After installing the package, you will need to import it in a python environment. After doing so, you can start divinng into company specifications. You can do this by implementing the following code snippet:

```
import ratio_analysis

company1 = ratio_analysis.Company_Analysis("company_name",year_of_analysis)

```
or by using a more direct approach

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
company1_liq_analysis = company1.liquidity_analysis(net_income,
                                                    total_stockholders_equity,
                                                    total_current_assets,
                                                    total_current_liabilities,
                                                    total_cash)
roe = company1_liq_analysis.return_on_equity()
print(roe)
```
## Solvency Analysis

In order to perform solvency analysis, you must have information regarding the company's total_liabilities, total stockholders' equity, and total assets. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_sol_analysis = company1.solvency_analysis(total_liabilities,
                                                   total_stockholders_equity,
                                                   total_assets)

```
After doing so, you can perform the following ratios: debt_to_equity(),debt_to_assets(), and financial_leverage_ratio().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_sol_analysis = company1.solvency_analysis(total_liabilities,
                                                   total_stockholders_equity,
                                                   total_assets)
d_t_e = company1_liq_analysis.debt_to_equity()
print(d_t_e)
```
## Profitability Analysis

In order to perform profitability analysis, you must have information regarding the company's net income, sales, gross profit, operating profit, and total assets. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_prof_analysis = company1.solvency_analysis(net_income,
                                                   sales,
                                                   gross_profit,
                                                   operating_profit,
                                                   total_assets)

```
After doing so, you can perform the following ratios: gross_profit_margin(),operatinng_profit_margin(), net_profit_marginn(), annd return_on_assets().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_prof_analysis = company1.solvency_analysis(net_income,
                                                   sales,
                                                   gross_profit,
                                                   operating_profit,
                                                   total_assets)
g_p_m = company1_prof_analysis.gross_profit_margin()
print(g_p_m)
```

## Turnover Analysis

In order to perform a turnnover analysis, you must have information regarding the company's cost of goods sold, average_inventory, sales, working capital, credit sales, average total assets, average accounts receivables, average capital employed, supplier purchases, and average accounts payables. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_turnov_analysis = company1.turnover_analysis(cogs,
                                                      average_innnventory,
                                                      sales,
                                                      working_capital,
                                                      credit_sales,
                                                      average_total_assets,
                                                      average_accounts_receivables,
                                                      average_capital_employed,
                                                      supplier_purchases,
                                                      average_accounts_payables)

```
After doing so, you can perform the following ratios: inventory_turnover(),receivables_turnover(), working_capital_turnover(), asset_turnover(), capital_employed_turnover(), and accounts_payable_turnover().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_turnov_analysis = company1.turnover_analysis(cogs,
                                                      average_innnventory,
                                                      sales,
                                                      working_capital,
                                                      credit_sales,
                                                      average_total_assets,
                                                      average_accounts_receivables,
                                                      average_capital_employed,
                                                      supplier_purchases,
                                                      average_accounts_payables)
inv_turnov = company1_turnov_analysis.inventory_turnover()
print(inv_turnov)
```
## Earnings Analysis

In order to perform a earnings analysis, you must have information regarding the company's earnings and number of shares outstanding. Furthermore, you will need to assign these values to the company object in a specific order.

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_earn_analysis = company1.earnings_analysis(earnings, number_of shares_outstanding)

```
After doing so, you can perform the following ratio: earnings_per_share().

```
from ratio_analysis import Company_Analysis

company1 = Company_Analysis("company_name",year_of_analysis)
company1_earn_analysis = company1.earnings_analysis(earnings, number_of shares_outstanding)
e_p_s = company1_earn_analysis.earnings_per_share()
print(e_p_s)
```





