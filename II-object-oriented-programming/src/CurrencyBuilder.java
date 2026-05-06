import currencies.*;

public class CurrencyBuilder
{
    private final CurrencyManager _currencyManager;

    public CurrencyBuilder(CurrencyManager currencyManager)
    {
        _currencyManager = currencyManager;
    }

    public void CreateCurrency(String name, String acronym, String symbol, double exchangeRate)
    {
        for (ValueCurrency currency : _currencyManager.GetCurrencies().keySet())
        {
            if (currency.Name.equalsIgnoreCase(name)) {
                System.out.println("The currency with name " + name + " already exists. Returning the currency instance.");
                return;
            }
        }

        ValueCurrency currency = switch (name.toUpperCase()) {
            case "REAL" -> new Real(name, acronym, symbol);
            case "DOLLAR" -> new Dollar(name, acronym, symbol);
            case "EURO" -> new Euro(name, acronym, symbol);
            default -> throw new RuntimeException("Invalid currency name.");
        };

        _currencyManager.GetCurrencies().put(currency, exchangeRate);
    }
}