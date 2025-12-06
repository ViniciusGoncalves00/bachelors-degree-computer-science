package deprecated;

import java.util.HashMap;

public class WalletDeprecated
{
    public final String Owner;
    public final HashMap<ValueCurrencyDeprecated, Double> Currencies;

    public WalletDeprecated(String owner) {
        Owner = owner;
        Currencies = new HashMap<>();
    }

    public String getInfo()
    {
        StringBuilder builder = new StringBuilder();
        builder.append("Owner: ").append(Owner).append("\n");

        for (ValueCurrencyDeprecated currency : Currencies.keySet())
        {
            builder.append(currency.Name)
                    .append(": ")
                    .append(currency.Symbol)
                    .append(" ")
                    .append(Currencies.get(currency))
                    .append("\n");
        }

        return builder.toString();
    }

    public String GetConvertedInfo(ValueCurrencyDeprecated target)
    {
        double currentAmount = Currencies.get(target);
        double defaultCurrencyAmount = 0;

        for (ValueCurrencyDeprecated currency : Currencies.keySet())
        {
            if (currency.equals(target))
            {
                continue;
            }

            defaultCurrencyAmount += Currencies.get(currency) * currency.ExchangeRate;
        }

        double rate = 1 / target.ExchangeRate;
        double convertedCurrency = defaultCurrencyAmount * rate;
        currentAmount += convertedCurrency;
        return target.Name + ": " + target.Symbol + " " + currentAmount;
    }

    public void Add(ValueCurrencyDeprecated currency, double amount)
    {
        if (Currencies.containsKey(currency))
        {
            double currentAmount = Currencies.get(currency);
            Currencies.put(currency, currentAmount + amount);
        }
        else
        {
            Currencies.put(currency, amount);
        }
    }
}