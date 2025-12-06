import currencies.ValueCurrency;

import java.util.HashMap;

public class Wallet
{
    public final int ID;
    public final String Owner;
    public final HashMap<ValueCurrency, Double> Currencies;

    public Wallet(int id, String owner)
    {
        ID = id;
        Owner = owner;
        Currencies = new HashMap<>();
    }

    public String GetInfo()
    {
        var info = new StringBuilder();
        info.append("Owner: ").append(Owner).append("\n");

        for (ValueCurrency currency : Currencies.keySet())
        {
            info.append(currency.Name)
                    .append(": ")
                    .append(currency.Symbol)
                    .append(" ")
                    .append(Currencies.get(currency))
                    .append("\n");
        }

        return info.toString();
    }

    public void AddCurrency(ValueCurrency currency, double amount)
    {
        HandleCurrency(currency, amount, 1);
    }

    public void SubtractCurrency(ValueCurrency currency, double amount)
    {
        HandleCurrency(currency, amount, -1);
    }

    private void HandleCurrency(ValueCurrency currency, double amount, int operation)
    {
        if (Currencies.containsKey(currency))
        {
            Currencies.compute(currency, (k, currentAmount) -> currentAmount + (amount * operation));
        }
        else
        {
            Currencies.put(currency, amount);
        }
    }
}