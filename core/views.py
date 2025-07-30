from django.shortcuts import render
from .models import Portfolio

def home(request):
    returns = Portfolio.objects.all().order_by('-start_date')  # latest first
    return render(request, 'home.html', {'returns': returns})

def about(request):
    return render(request, 'about.html')

def nebula(request):
    return render(request, 'nebula.html')

def voyager(request):
    return render(request, 'voyager.html')

"""
p = Portfolio.objects.create(
    framework='Value Investing',
    start_date=date(2024, 1, 1),
    init_amt=Decimal('100000.00')
)

Holding.objects.create(
    portfolio=p,
    ticker='AAPL',
    buy_price=Decimal('180.50'),
    quantity=Decimal('50'),
    buy_date=date(2024, 1, 5)
)

Holding.objects.create(
    portfolio=p,
    ticker='GOOG',
    buy_price=Decimal('2800.00'),
    quantity=Decimal('10'),
    buy_date=date(2024, 1, 7)
)

QUERYYYYYYYYYYY

portfolios = Portfolio.objects.all()
p = Portfolio.objects.get(id=1)
holdings = p.holdings.all()

aapl_holdings = Holding.objects.filter(ticker='AAPL')

for h in p.holdings.all():
    print(f"{h.ticker}: {h.quantity} shares bought at {h.buy_price}")




"""
