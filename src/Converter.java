import currencies.ValueCurrency;

public class Converter
{
    private final CurrencyManager _currencyManager;

    public Converter(CurrencyManager currencyManager)
    {
        _currencyManager = currencyManager;
    }

    public String Convert(Wallet wallet, ValueCurrency currencyTarget)
    {
        double currentAmount = wallet.Currencies.get(currencyTarget);
        double defaultCurrencyAmount = 0;

        for (ValueCurrency currency : wallet.Currencies.keySet())
        {
            if (currency.equals(currencyTarget))
            {
                continue;
            }

            double exchangeRate = _currencyManager.GetCurrencies().get(currency);
            defaultCurrencyAmount += wallet.Currencies.get(currency) * exchangeRate;
        }

        double targetExchangeRate = _currencyManager.GetCurrencies().get(currencyTarget);
        double rate = 1 / targetExchangeRate;
        double convertedCurrency = defaultCurrencyAmount * rate;
        currentAmount += convertedCurrency;
        return currencyTarget.Name + ": " + currencyTarget.Symbol + " " + currentAmount;
    }
}