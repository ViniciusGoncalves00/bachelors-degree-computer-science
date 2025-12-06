public class WalletBuilder
{
    private final WalletManager _walletManager;

    public WalletBuilder(WalletManager currencyManager)
    {
        _walletManager = currencyManager;
    }

    public void CreateWallet(String owner)
    {
        var wallets = _walletManager.GetWallets();
        var id = wallets.toArray().length;
        var wallet = new Wallet(id, owner);
        wallets.add(wallet);
    }
}