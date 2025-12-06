import currencies.ValueCurrency;

import java.util.ArrayList;
import java.util.Scanner;

public class UserInterface
{
    private static UserInterface _instance;
    private final Scanner _scanner;

    private final String[] _mainOptions =
            {
                    "Exit.",
                    "Create a new wallet.",
                    "Create a new currency.",
                    "See existing wallets.",
                    "See existing currencies.",
                    "Manipulate wallets."
            };

    private final String[] _exitOptions =
            {
                    "Yes.",
                    "No.",
            };
    private final String[] _createWalletOptions =
            {
                    "0 - Return to main menu.",
                    "Insert wallet owner name:",
            };
    private final String[] _createCurrencyOptions =
            {
                    "0 - Return to main menu.",
                    "Insert currency name:",
                    "Insert symbol name:",
                    "Insert currency exchange rate to dollar:",
            };
    private final String[] _manipulateWalletOptions =
            {
                    "Return to main menu.",
                    "Get info:",
                    "Add currency:",
                    "Remove currency:",
                    "Convert currency:",
            };

    private UserInterface()
    {
        _scanner = new Scanner(System.in);

        for(int i = 0; i < _mainOptions.length; i++)
            _mainOptions[i] = i + " - " + _mainOptions[i];

        for(int i = 0; i < _exitOptions.length; i++)
            _exitOptions[i] = i + " - " + _exitOptions[i];

        for(int i = 0; i < _manipulateWalletOptions.length; i++)
            _manipulateWalletOptions[i] = i + " - " + _manipulateWalletOptions[i];
    }

    public static UserInterface GetInstance()
    {
        if(_instance == null)
        {
            _instance = new UserInterface();
        }

        return _instance;
    }

    public void NewInterface()
    {
        System.out.println("Welcome to your Currency Wallet!");

        Interface();
    }

    private void Interface()
    {
        var optionSelected = MainMenu();
        String info;

        switch (optionSelected)
        {
            case 0:
                optionSelected = ExitMenu();
                break;
            case 1:
                CreateWalletMenu();
                break;
            case 2:
                CreateCurrencyMenu();
                break;
            case 3:
                info = SystemManager.GetInstance().walletManager.GetInfo();
                System.out.println(info);
                break;
            case 4:
                info = SystemManager.GetInstance().currencyManager.GetInfo();
                System.out.println(info);
                break;
            case 5:
                ManipulateWallet();
                break;
            default:
                break;
        }

        if (optionSelected != 0)
            Interface();
    }

    private int MainMenu()
    {
        System.out.println("Please select an option:");
        for (String option : _mainOptions)
            System.out.println(option);

        return _scanner.nextInt();
    }

    private int ExitMenu()
    {
        System.out.println("You're sure?");
        for (String option : _exitOptions)
            System.out.println(option);

        var input = _scanner.nextInt();

        if (input != 0)
            DefaultMessage();

        return input;
    }

    private void CreateWalletMenu()
    {
        for (String option : _createWalletOptions)
            System.out.println(option);

        var input = _scanner.next();
        if (input.equals("0"))
        {
            System.out.println("Creation of an new wallet is cancelled.");
            DefaultMessage();
            return;
        }

        SystemManager.GetInstance().walletBuilder.CreateWallet(input);

        System.out.println("Wallet created!");
        DefaultMessage();
    }

    private void CreateCurrencyMenu()
    {
        System.out.println("0 - Return to main menu.");
        System.out.println("Insert currency name:");
        var name = _scanner.next();

        if (name.equals("0"))
        {
            System.out.println("Creation of an new currency is cancelled.");
            DefaultMessage();
            return;
        }

        System.out.println("0 - Return to main menu.");
        System.out.println("Insert acronym:");
        var acronym = _scanner.next();

        if (acronym.equals("0"))
        {
            System.out.println("Creation of an new currency is cancelled.");
            DefaultMessage();
            return;
        }

        System.out.println("0 - Return to main menu.");
        System.out.println("Insert symbol:");
        var symbol = _scanner.next();

        if (symbol.equals("0"))
        {
            System.out.println("Creation of an new currency is cancelled.");
            DefaultMessage();
            return;
        }

        System.out.println("0 - Return to main menu.");
        System.out.println("Insert currency exchange rate to dollar:");
        var exchangeRate = _scanner.next();

        if (exchangeRate.equals("0"))
        {
            System.out.println("Creation of an new currency is cancelled.");
            DefaultMessage();
            return;
        }

        SystemManager.GetInstance().currencyBuilder.CreateCurrency(name, acronym, symbol, Double.parseDouble(exchangeRate));

        System.out.println("Currency created!");
        DefaultMessage();
    }

    private void ManipulateWallet()
    {
        System.out.println("Select Wallet:");
        var wallets = SystemManager.GetInstance().walletManager.GetWallets();

        for (int i = 0; i < wallets.size(); i++) {
            System.out.println(i + " - " + wallets.get(i).GetInfo());
        }

        var index = _scanner.nextInt();

        if (index < 0 || index >= wallets.size()) {
            System.out.println("Invalid wallet index.");
            DefaultMessage();
            return;
        }

        var wallet = wallets.get(index);

        for (String option : _manipulateWalletOptions) {
            System.out.println(option);
        }

        ValueCurrency currency;
        double amount;

        index = _scanner.nextInt();
        switch (index) {
            case 0:
                System.out.println("Operation cancelled.");
                DefaultMessage();
                return;
            case 1:
                System.out.println(wallet.GetInfo());
                break;
            case 2:
                System.out.println(SystemManager.GetInstance().currencyManager.GetInfo());
                var currencies = new ArrayList<>(SystemManager.GetInstance().currencyManager.GetCurrencies().keySet());

                System.out.println("Select currency index:");
                index = _scanner.nextInt();

                if (index < 0 || index >= currencies.size()) {
                    System.out.println("Invalid currency index.");
                    DefaultMessage();
                    return;
                }

                currency = currencies.get(index);
                System.out.println("Input amount:");
                amount = _scanner.nextDouble();

                wallet.AddCurrency(currency, amount);
                break;
            case 3:
                System.out.println(wallet.GetInfo());
                System.out.println("Select currency index:");
                currencies = new ArrayList<>(wallet.Currencies.keySet());
                index = _scanner.nextInt();

                if (index < 0 || index >= currencies.size()) {
                    System.out.println("Invalid currency index.");
                    DefaultMessage();
                    return;
                }

                currency = currencies.get(index);
                System.out.println("Input amount to subtract:");
                amount = _scanner.nextDouble();

                wallet.SubtractCurrency(currency, amount);
                break;
            case 4:
                System.out.println(SystemManager.GetInstance().currencyManager.GetInfo());
                currencies = new ArrayList<>(SystemManager.GetInstance().currencyManager.GetCurrencies().keySet());
                System.out.println("Input target currency:");

                System.out.println("Select currency index:");
                index = _scanner.nextInt();

                if (index < 0 || index >= currencies.size()) {
                    System.out.println("Invalid currency index.");
                    DefaultMessage();
                    return;
                }

                var currencyTarget = currencies.get(index);
                var convertedValue = SystemManager.GetInstance().converter.Convert(wallet, currencyTarget);
                System.out.println("Converted value: " + convertedValue);
                break;
            default:
                System.out.println("Invalid option.");
                DefaultMessage();
        }

        System.out.println("Operation succeed!");
        DefaultMessage();
    }

    private void DefaultMessage()
    {
        System.out.println("Returning to main menu!");
    }
}