public class SystemManager
{
    private static SystemManager _instance;

    public final UserInterface userInterface;
    public final WalletManager walletManager;
    public final WalletBuilder walletBuilder;
    public final CurrencyManager currencyManager;
    public final CurrencyBuilder currencyBuilder;
    public final Converter converter;

    private SystemManager()
    {
        userInterface = UserInterface.GetInstance();
        walletManager = WalletManager.GetInstance();
        walletBuilder = new WalletBuilder(walletManager);
        currencyManager = CurrencyManager.GetInstance();
        currencyBuilder = new CurrencyBuilder(currencyManager);
        converter = new Converter(currencyManager);
    }

    public static SystemManager GetInstance()
    {
        if(_instance == null)
        {
            _instance = new SystemManager();
        }

        return _instance;
    }
}