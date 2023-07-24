def get_last_price(ticker: str) -> float:
    """
    Esta funcion busca usando la API de yahoo finance el ultimo precio disponible del instrumento cuyo ticker es 'ticker'.
    @:param ticker: ticker de la empresa a consultar
    """
    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    # yahoo_finance_url = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker  # lo mismo que arriba
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('chart') is None:
        raise ValueError(f"ticker: '{ticker}' not found")

    price = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')

    print(r.json())
    return price

def get_list_elements(ticker: str):
    """
    Esta funcion busca usando la API de yahoo finance varios elementos en función de  cuyo ticker es 'ticker'.
    @:param ticker: ticker de la empresa a consultar
    """
    elements = []
    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    # yahoo_finance_url = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker  # lo mismo que arriba
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('chart') is None:
        raise ValueError(f"ticker: '{ticker}' not found")
    print(r.json())
    cu = r.json().get('chart').get('result')[0].get('meta').get('currency')
    sy = r.json().get('chart').get('result')[0].get('meta').get('symbol')
    ex = r.json().get('chart').get('result')[0].get('meta').get('exchangeTimezoneName')
    pc = r.json().get('chart').get('result')[0].get('meta').get('previousClose')
    pa = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')

    for i in (cu,sy,ex,pc,pa):
      elements.append(i)

    return elements

