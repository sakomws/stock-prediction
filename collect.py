import csv
import sys
import transport as tp
from yahoofinancials import YahooFinancials as YF
import main

class Collect:
    def __init__(self,ticker):
        self.tick = YF(ticker)
        self.d_stock = self.tick.get_historical_price_data('2008-01-01', '2019-01-01', 'daily')
        self.a_income = self.tick.get_financial_stmts('annual', 'income')
        self.a_balance = self.tick.get_financial_stmts('annual', 'balance')
        self.a_cash = self.tick.get_financial_stmts('annual', 'cash')

    def data_collect(self):
        try:
            r = self.tick._cache.keys()
        except AttributeError:
            pass
        else:
            print(main.mark)
            print(r)

    def print_console(self):
        print(main.mark)
        print('Statistic Analysis:')
        print('===============================================')
        print('Stock Exchange Data Source: ', self.tick.get_stock_exchange())
        print('Currency: ', self.tick.get_currency())
        print(main.mark)
        print('Valuation Measures')
        print(main.mark)
        print('main.market CAP: ',self.tick.get_market_cap())
        print('PE(Price to Earnings Ratio): ', self.tick.get_pe_ratio())
        print('Price to Sales: ', self.tick.get_price_to_sales())
        print(main.mark)
        print('Stock Measures')
        print(main.mark)
        print('Current Price: ',self.tick.get_current_price())
        print('Current Change: ', self.tick.get_current_change())
        print('Current percent change',self.tick.get_current_percent_change())
        print('Current volume: ',self.tick.get_current_volume())
        print('Daily Low: ', self.tick.get_daily_low())
        print('Daily High:', self.tick.get_daily_high())
        print('Yearly high: ', self.tick.get_yearly_high())
        print('Yearly Low: ', self.tick.get_yearly_low())
        print('50 day moving avg: ',self.tick.get_50day_moving_avg())
        print('200day moving avg: ',self.tick.get_200day_moving_avg())
        print('Previous day close price: ',self.tick.get_prev_close_price())
        print('Open price: ',self.tick.get_open_price())
        print('10days Average daily volume: ',self.tick.get_ten_day_avg_daily_volume())
        print('30 days Average daily volume: ',self.tick.get_three_month_avg_daily_volume())
        print('Beta(3y monthly), stock volatility(>1, risky but profitable): ',self.tick.get_beta())
        print(main.mark)
        print('Financial Highlights: Income/Cash/Balance Sheet')
        print(main.mark)
        print('Interest Expense: ',self.tick.get_interest_expense())
        print('Operating Income: ', self.tick.get_operating_income())
        print('Total Operating Expense: ',self.tick.get_total_operating_expense())
        print('Total Revenue: ',self.tick.get_total_revenue())
        print('Cost of Revenue: ',self.tick.get_cost_of_revenue())
        print('Income Before Tax: ',self.tick.get_income_before_tax())
        print('Income Tax Expense: ',self.tick.get_income_tax_expense())
        print('Gross Profit', self.tick.get_gross_profit())
        print('Net Income: ', self.tick.get_net_income())
        print('Net Income from Continuing Ops: ',self.tick.get_net_income_from_continuing_ops())
        print('Research and Development Cost: ',self.tick.get_research_and_development())
        print('Book Value(Net Asset=TotalAsset-IntangibleAsset(Patent,Goodwill)): ',self.tick.get_book_value())
        print('EBITDA(Earnings before interest,tax depreciation and amartization): ',self.tick.get_ebit())
        print('Earnings per share: ',self.tick.get_earnings_per_share())
        print(main.mark)
        print('Dividents and splits, Currently, missing in YahooFinancials as well')
        print(main.mark)
        print('Divindent Yield',self.tick.get_dividend_yield())
        print('Annual average Divident yield: ',self.tick.get_annual_avg_div_yield())
        print('5y average divident yield: ',self.tick.get_five_yr_avg_div_yield())
        print('Dividend Rate: ',self.tick.get_dividend_rate())
        print('Annual average dividend rate',self.tick.get_annual_avg_div_rate())
        print('Payout Ratio: ',self.tick.get_payout_ratio())
        print('Ex Evidend Date: ',self.tick.get_exdividend_date())

    def save_csv(self):

        # Save Stock Prices in CSV
        with open('Stock_prices_'+ main.company +'.csv', mode='w') as result_w:
            result = csv.writer(result_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow(['Date', 'high', 'low', 'adjclose', 'close', 'open', 'volume'])
            for k,v in self.d_stock['GOOGL'].items():
                if k=='prices':
                    for i in v:
                        transport(v)
                        result.writerow([i['formatted_date'],i['high'],i['low'],i['adjclose'],i['close'],i['open'],i['volume']])

        # Save Annual Income Statement in CSV
        with open('Annual_Income_statement_' + main.company + '.csv', mode='w') as result_w:
            result = csv.writer(result_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow(['Year', 'researchDevelopment', 'incomeBeforeTax', 'minorityInterest', 'netIncome',
                             'effectOfAccountingCharges', 'sellingGeneralAdministrative', 'grossProfit', 'ebit',
                             'operatingIncome', 'otherOperatingExpenses', 'interestExpense', 'extraordinaryItems',
                             'nonRecurring', 'otherItems', 'incomeTaxExpense', 'totalRevenue', 'totalOperatingExpenses',
                             'costOfRevenue', 'totalOtherIncomeExpenseNet', 'discontinuedOperations',
                             'netIncomeFromContinuingOps', 'netIncomeApplicableToCommonShares'])
            for i in self.a_income['incomeStatementHistory']['GOOGL']:
                for k, v in i.items():
                    tp.transport(v)
                    result.writerow(
                                 [k, v['researchDevelopment'], v['incomeBeforeTax'], v['minorityInterest'], v['netIncome'],
                                 v['effectOfAccountingCharges'], v['sellingGeneralAdministrative'], v['grossProfit'],
                                 v['ebit'], v['operatingIncome'], v['otherOperatingExpenses'], v['interestExpense'],
                                 v['extraordinaryItems'], v['nonRecurring'], v['otherItems'], v['incomeTaxExpense'],
                                 v['totalRevenue'], v['totalOperatingExpenses'], v['costOfRevenue'],
                                 v['totalOtherIncomeExpenseNet'], v['discontinuedOperations'],
                                 v['netIncomeFromContinuingOps'], v['netIncomeApplicableToCommonShares']])

        # Save Annual Balance Sheet in CSV
        with open('Annual_Balance_Sheet_' + main.company + '.csv', mode='w') as result_w:
            result = csv.writer(result_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow(['Year', 'intangibleAssets', 'totalLiab', 'totalStockholderEquity', 'otherCurrentLiab', 'totalAssets',
                             'commonStock', 'otherCurrentAssets', 'retainedEarnings', 'otherLiab', 'goodWill', 'treasuryStock',
                             'otherAssets', 'cash', 'totalCurrentLiabilities', 'deferredLongTermAssetCharges', 'otherStockholderEquity',
                             'propertyPlantEquipment', 'totalCurrentAssets', 'longTermInvestments', 'netTangibleAssets',
                             'shortTermInvestments', 'netReceivables', 'longTermDebt', 'accountsPayable'])
            for i in self.a_balance['balanceSheetHistory']['GOOGL']:
                for k, v in i.items():
                    tp.transport(v)
                    result.writerow(
                                [k, v['intangibleAssets'], v['totalLiab'], v['totalStockholderEquity'], v['otherCurrentLiab'],
                                v['totalAssets'], v['commonStock'], v['otherCurrentAssets'], v['retainedEarnings'], v['otherLiab'],
                                v['goodWill'], v['treasuryStock'], v['otherAssets'], v['cash'], v['totalCurrentLiabilities'],
                                v['deferredLongTermAssetCharges'], v['otherStockholderEquity'],
                                v['propertyPlantEquipment'], v['totalCurrentAssets'], v['longTermInvestments'],
                                v['netTangibleAssets'], v['shortTermInvestments'], v['netReceivables'], v['longTermDebt'],
                                v['accountsPayable']])

        # Save Annual Cash Flow in CSV
        with open('Annual_Cash_Flow_' + main.company + '.csv', mode='w') as result_w:
            result = csv.writer(result_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow(['Year', 'investments', 'changeToLiabilities', 'totalCashflowsFromInvestingActivities', 'netBorrowings',
                             'totalCashFromFinancingActivities', 'changeToOperatingActivities', 'netIncome', 'changeInCash',
                             'repurchaseOfStock', 'effectOfExchangeRate', 'totalCashFromOperatingActivities', 'depreciation',
                             'otherCashflowsFromInvestingActivities', 'changeToAccountReceivables', 'otherCashflowsFromFinancingActivities',
                             'changeToNetincome', 'capitalExpenditures'])
            for i in self.a_cash['cashflowStatementHistory']['GOOGL']:
                for k, v in i.items():
                    tp.transport(v)
                    result.writerow(
                        [k, v['investments'], v['changeToLiabilities'], v['totalCashflowsFromInvestingActivities'], v['netBorrowings'],
                         v['totalCashFromFinancingActivities'], v['changeToOperatingActivities'], v['netIncome'], v['changeInCash'],
                         v['repurchaseOfStock'], v['effectOfExchangeRate'], v['totalCashFromOperatingActivities'], v['depreciation'],
                         v['otherCashflowsFromInvestingActivities'], v['changeToAccountReceivables'], v['otherCashflowsFromFinancingActivities'],
                         v['changeToNetincome'], v['capitalExpenditures']])