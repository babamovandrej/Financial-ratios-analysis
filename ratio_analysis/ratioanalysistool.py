class Company_Analysis:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    class liquidity_analysis():

        def __init__(self,
                     net_income,
                     total_stockholders_equity,
                     total_current_assets,
                     total_current_liabilities,
                     total_cash,
                     ):
            self.net_income = net_income
            self.total_stockholders_equity = total_stockholders_equity
            self.total_current_assets = total_current_assets
            self.total_current_liabilities = total_current_liabilities
            self.total_cash = total_cash

        def return_on_equity(self):
            roe = (self.net_income / self.total_stockholders_equity)*100
            return str(roe)+'%'

        def current_ratio(self):
            curr_ratio = self.total_current_assets/self.total_current_liabilities
            return curr_ratio

        def cash_ratio(self):
            cash_ratio = (self.total_cash/self.total_current_liabilities)*100
            return cash_ratio

        def net_working_capital(self):
            nwc = self.total_current_assets - self.total_current_liabilities
            return nwc

    class solvency_analysis():

        def __init__(self,
                     total_liabilities,
                     total_stockholders_equity,
                     total_assets
                     ):
            self.total_liabilities = total_liabilities
            self.total_stockholders_equity = total_stockholders_equity
            self.total_assets = total_assets

        def debt_to_equity(self):
            d_t_e = self.total_liabilities/self.total_stockholders_equity
            return str(d_t_e)+'%'

        def debt_to_assets(self):
            d_t_a = self.total_liabilities/self.total_assets
            return str(d_t_a)+'%'

        def financial_leverage_ratio(self):
            f_l_r = self.total_assets / self.total_stockholders_equity
            return round(f_l_r, 3)

    class profitability_analysis():

        def __init__(self,
                     net_income,
                     sales,
                     gross_profit,
                     operating_profit,
                     total_assets
                     ):
            self.net_income = net_income
            self.sales = sales
            self.gross_profit = gross_profit
            self.operating_profit = operating_profit
            self.total_assets = total_assets

        def gross_profit_margin(self):
            g_p_m = (self.gross_profit / self.sales) * 100
            return str(g_p_m)+"%"

        def operating_profit_margin(self):
            o_p_m = (self.operating_profit/self.sales) * 100
            return str(o_p_m)+'%'

        def net_profit_margin(self):
            net_p_m = (self.net_income/self.sales) * 100
            return str(net_p_m)+"%"

        def return_on_assets(self):
            roa = (self.net_income/self.total_assets) * 100
            return str(roa)+"%"

    class turnover_analysis():

        def __init__(self,
                     cogs,
                     average_inventory,
                     sales,
                     working_capital,
                     credit_sales,
                     average_total_assets,
                     average_accounts_receivables,
                     average_capital_employed,
                     supplier_purchases,
                     average_accounts_payables):
            self.cogs = cogs,
            self.average_inventory = average_inventory,
            self.sales = sales,
            self.working_capital = working_capital,
            self.credit_sales = credit_sales,
            self.average_total_assets = average_total_assets,
            self.average_accounts_receivables = average_accounts_receivables,
            self.average_capital_employed = average_capital_employed,
            self.supplier_purchases = supplier_purchases,
            self.average_accounts_payables = average_accounts_payables

        def inventory_turnover(self):
            inventory_turnov = (self.cogs/self.average_inventory)
            return inventory_turnov

        def receivables_turnover(self):
            receivables_turnov = (
                self.credit_sales/self.average_accounts_receivables)
            return receivables_turnov

        def working_capital_turnover(self):
            w_c_turnov = (self.sales/self.working_capital)
            return w_c_turnov

        def asset_turnover(self):
            asset_turnov = (self.sales/self.average_total_assets)
            return asset_turnov

        def capital_employed_turnover(self):
            capital_em_turnov = (self.sales/self.average_capital_employed)
            return capital_em_turnov

        def accounts_payable_turnover(self):
            acc_payable_turnov = (
                self.supplier_purchases/self.average_accounts_payables)
            return acc_payable_turnov

    class earnings_analysis():

        def __init__(self,
                     earnings,
                     number_of_shares_outstanding):

            self.earnings = earnings
            self.number_of_shares_outstanding = number_of_shares_outstanding

        def earnings_per_share(self):
            e_p_s = (self.earnings/self.number_of_shares_outstanding)
            return e_p_s
