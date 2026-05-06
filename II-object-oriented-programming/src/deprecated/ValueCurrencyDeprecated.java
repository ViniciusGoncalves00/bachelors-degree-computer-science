package deprecated;

public class ValueCurrencyDeprecated
{
    public final String Name;
    public final String Symbol;
    public final double ExchangeRate;

    public ValueCurrencyDeprecated(String name, String symbol, double exchangeRate) {
        Name = name;
        Symbol = symbol;
        ExchangeRate = exchangeRate;
    }

    public String getInfo() { return "Name: " + ", Symbol: " + Symbol; }
}