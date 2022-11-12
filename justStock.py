import napkin

@napkin.seq_diagram()
def stock_Flow(c):
    user = c.object('user')
    companyRanks = c.object('companyRanks')
    companyStocks = c.object('companyStocks')
    database  = c.object('database')
    API = c.object('API')
    
    with user:
        with companyRanks.getRankedCompany():
            with API.getCompanyData():
                with database.postCompanyData():
                    API.receiveCompanyData().ret('StructuredResponse')
                    companyRanks.getCompanyData('CompanyRanks')
        with companyStocks.getStocksCompany():
            with API.getStocksCompanyData():
                with database.postStocksCompanyData():
                    API.recieveStocksCompanyData().ret('structuredResponse')
                    companyStocks.getStocksCompany('CompanyStocksMarketInfo')