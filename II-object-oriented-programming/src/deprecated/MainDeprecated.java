package deprecated;

public class MainDeprecated
{
    public static void mainDeprecated(String[] args) {
        ValueCurrencyDeprecated real = new ValueCurrencyDeprecated("Real", "R$", 0.17);
        ValueCurrencyDeprecated dollar = new ValueCurrencyDeprecated("Dollar", "$", 1);
        ValueCurrencyDeprecated euro = new ValueCurrencyDeprecated("Euro", "€", 1.07);

        WalletDeprecated wallet = new WalletDeprecated("Vinicius");
        wallet.Add(real, 1412);
        wallet.Add(dollar, 11.09);
        wallet.Add(euro, 19.45);

        System.out.println(wallet.getInfo());
        System.out.println(wallet.GetConvertedInfo(real));
        System.out.println(wallet.GetConvertedInfo(dollar));
        System.out.println(wallet.GetConvertedInfo(euro));
    }
}