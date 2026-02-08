import os, sys, time, requests, re, random
from pyfiglet import Figlet
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    custom_fig = Figlet(font='ansi_shadow')
    logo = custom_fig.renderText("TRADING TOOLS")
    print("\033[1;96m" + logo)
    print("\033[1;91m" + "═"*50)
    print("\033[1;92m║\033[1;97m[+] DEVELOPER   : \033[1;92mPLANALTO                \033[1;92m║")
    print("\033[1;92m║\033[1;97m[+] TELEGRAM    : \033[1;92mhttps://t.me/planaltocc \033[1;92m║")
    print("\033[1;92m║\033[1;97m[+] VERSION     : \033[1;92m01:00                   \033[1;92m║")
    print("\033[1;92m║\033[1;97m[+] TOOLS       : \033[1;92mTRADING SIGNAL GENERATOR\033[1;92m║")
    print("\033[1;91m" + "═"*50)

def loading_animation(duration=2):
    animation = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in animation:
            sys.stdout.write(f"\r\033[1;93mInitializing System... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r\033[1;93mSystem Ready!          ")

def generate_demo_signals(pairs, days, min_percent, mode):
    """Generate demo trading signals for testing"""
    signals = []
    for pair in pairs:
        # Remove OTC suffix for display
        display_pair = pair.replace("-OTC", "")
        
        # Generate random but realistic signal data
        trend = random.choice(["BUY", "SELL"])
        confidence = random.randint(min_percent, 95)
        price = round(random.uniform(1.0, 200.0), 4)
        target = round(price * (1 + random.uniform(0.01, 0.05)), 4)
        stop_loss = round(price * (1 - random.uniform(0.005, 0.02)), 4)
        
        signals.append({
            'pair': display_pair,
            'signal': trend,
            'confidence': f"{confidence}%",
            'entry': price,
            'target': target,
            'stop_loss': stop_loss,
            'risk_reward': f"1:{round((target-price)/(price-stop_loss), 2)}"
        })
    
    return signals

def main():
    clear_screen()
    display_logo()
    loading_animation()
    
    print("\n\033[1;92m" + "═"*50)
    print("\033[1;92m║\033[1;97m       WELCOME - NO LOGIN REQUIRED          \033[1;92m║")
    print("\033[1;92m║\033[1;97m     TRADING SIGNAL GENERATOR v1.0          \033[1;92m║")
    print("\033[1;92m" + "═"*50 + "\n")
    
    # Get user name for personalization (optional)
    user_name = input("\033[1;92mEnter your name (optional, press Enter to skip): ")
    if user_name:
        print(f"\n\033[1;92mWelcome, {user_name}!\n")
    
    # Trading modes
    modes = {
        "1": {"name": "Scalping", "desc": "Short-term (5-15 min)"},
        "2": {"name": "Day Trading", "desc": "Intraday (1-4 hours)"},
        "3": {"name": "Swing Trading", "desc": "Medium-term (1-5 days)"},
        "4": {"name": "Position Trading", "desc": "Long-term (weeks-months)"}
    }
    
    print("\033[1;92mAvailable Trading Modes:")
    print("\033[1;93m" + "═"*40)
    for key, mode in modes.items():
        print(f"\033[1;93m{key}. \033[1;96m{mode['name']:20} \033[1;90m({mode['desc']})")
    print("\033[1;93m" + "═"*40)
    
    while True:
        mode_choice = input("\n\033[1;92mSelect trading mode (1-4): ")
        if mode_choice in modes:
            selected_mode = modes[mode_choice]
            break
        print("\033[1;91mInvalid choice. Please select 1-4")
    
    # Timeframe selection
    timeframes = {
        "1": "1 Minute",
        "2": "5 Minutes", 
        "3": "15 Minutes",
        "4": "1 Hour",
        "5": "4 Hours",
        "6": "1 Day"
    }
    
    print("\n\033[1;92mSelect Timeframe:")
    for key, tf in timeframes.items():
        print(f"\033[1;93m{key}. \033[1;96m{tf}")
    
    while True:
        tf_choice = input("\n\033[1;92mSelect timeframe (1-6): ")
        if tf_choice in timeframes:
            selected_tf = timeframes[tf_choice]
            break
        print("\033[1;91mInvalid choice. Please select 1-6")
    
    # Asset selection
    asset_categories = {
        "1": {"name": "Forex Majors", "pairs": [
            "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "USD/CHF-OTC",
            "AUD/USD-OTC", "USD/CAD-OTC", "NZD/USD-OTC"
        ]},
        "2": {"name": "Forex Minors", "pairs": [
            "EUR/GBP-OTC", "EUR/JPY-OTC", "GBP/JPY-OTC", "AUD/JPY-OTC",
            "EUR/CAD-OTC", "GBP/CAD-OTC", "AUD/CAD-OTC"
        ]},
        "3": {"name": "Cryptocurrencies", "pairs": [
            "BTC/USD-OTC", "ETH/USD-OTC", "XRP/USD-OTC", "LTC/USD-OTC",
            "BCH/USD-OTC", "ADA/USD-OTC", "DOT/USD-OTC"
        ]},
        "4": {"name": "Indices", "pairs": [
            "US30-OTC", "US500-OTC", "NAS100-OTC", "GER30-OTC",
            "UK100-OTC", "JPN225-OTC", "AUS200-OTC"
        ]},
        "5": {"name": "Commodities", "pairs": [
            "XAU/USD-OTC", "XAG/USD-OTC", "OIL-OTC", "GAS-OTC",
            "COPPER-OTC", "COFFEE-OTC", "SUGAR-OTC"
        ]}
    }
    
    print("\n\033[1;92mSelect Asset Category:")
    for key, category in asset_categories.items():
        print(f"\033[1;93m{key}. \033[1;96m{category['name']}")
    
    selected_pairs = []
    while True:
        cat_choice = input("\n\033[1;92mSelect category (1-5): ")
        if cat_choice in asset_categories:
            category = asset_categories[cat_choice]
            
            print(f"\n\033[1;92m{category['name']} Pairs:")
            print("\033[1;93m" + "═"*40)
            for i, pair in enumerate(category['pairs'], 1):
                display_pair = pair.replace("-OTC", "")
                print(f"\033[1;93m{i}. \033[1;96m{display_pair}")
            print("\033[1;93m" + "═"*40)
            
            # Select pairs
            while True:
                pair_input = input("\n\033[1;92mSelect pairs (e.g., 1,3,5 or 'all'): ")
                
                if pair_input.lower() == 'all':
                    selected_pairs = category['pairs']
                    break
                
                try:
                    choices = [int(c.strip()) for c in pair_input.split(',')]
                    valid_choices = all(1 <= c <= len(category['pairs']) for c in choices)
                    
                    if valid_choices:
                        selected_pairs = [category['pairs'][c-1] for c in choices]
                        break
                    else:
                        print(f"\033[1;91mInvalid choices. Please select 1-{len(category['pairs'])}")
                except:
                    print("\033[1;91mInvalid input. Please enter numbers like 1,3,5")
            
            break
        print("\033[1;91mInvalid category. Please select 1-5")
    
    # Risk management
    print("\n\033[1;92mRisk Management Settings:")
    print("\033[1;93m" + "═"*40)
    
    while True:
        try:
            risk_percent = float(input("\033[1;92mRisk per trade (0.5-5%): "))
            if 0.5 <= risk_percent <= 5:
                break
            print("\033[1;91mPlease enter between 0.5 and 5")
        except:
            print("\033[1;91mInvalid input")
    
    while True:
        try:
            account_size = float(input("\033[1;92mAccount size ($): "))
            if account_size > 0:
                break
            print("\033[1;91mPlease enter positive amount")
        except:
            print("\033[1;91mInvalid input")
    
    # Generate signals
    print("\n\033[1;93m" + "═"*60)
    print("\033[1;92mGENERATING TRADING SIGNALS...")
    print("\033[1;93m" + "═"*60)
    
    # Loading simulation
    for i in range(1, 11):
        sys.stdout.write(f"\r\033[1;93mAnalyzing market data... [{i*10}%] {'█'*i}{'░'*(10-i)}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n\n\033[1;92m" + "═"*80)
    print("\033[1;92m║\033[1;97m                    TRADING SIGNALS REPORT                    \033[1;92m║")
    print("\033[1;92m" + "═"*80)
    
    # Report header
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[1;97mDate/Time      : \033[1;92m{current_time}")
    print(f"\033[1;97mTrading Mode   : \033[1;92m{selected_mode['name']}")
    print(f"\033[1;97mTimeframe      : \033[1;92m{selected_tf}")
    print(f"\033[1;97mAccount Size   : \033[1;92m${account_size:,.2f}")
    print(f"\033[1;97mRisk per Trade : \033[1;92m{risk_percent}% (${account_size * risk_percent/100:.2f})")
    print("\033[1;92m" + "═"*80 + "\n")
    
    # Generate and display signals
    signals = generate_demo_signals(selected_pairs, 1, 65, selected_mode['name'])
    
    for idx, signal in enumerate(signals, 1):
        color = "\033[1;92m" if signal['signal'] == "BUY" else "\033[1;91m"
        
        print(f"\033[1;95m[TRADE {idx}] \033[1;97m{signal['pair']}")
        print(f"  Signal     : {color}{signal['signal']}\033[0m")
        print(f"  Confidence : \033[1;93m{signal['confidence']}")
        print(f"  Entry      : \033[1;97m{signal['entry']}")
        print(f"  Target     : \033[1;92m{signal['target']} (+{((signal['target']-signal['entry'])/signal['entry']*100):.2f}%)")
        print(f"  Stop Loss  : \033[1;91m{signal['stop_loss']} (-{((signal['entry']-signal['stop_loss'])/signal['entry']*100):.2f}%)")
        print(f"  Risk/Reward: \033[1;96m{signal['risk_reward']}")
        print(f"  Position   : \033[1;97m${account_size * risk_percent/100:.2f} risk")
        print("\033[1;90m" + "─"*50)
    
    # Trading advice
    print("\n\033[1;95m" + "═"*80)
    print("\033[1;92m║\033[1;97m                    TRADING ADVICE                         \033[1;92m║")
    print("\033[1;95m" + "═"*80)
    
    advice = [
        "✓ Always use stop-loss orders",
        "✓ Never risk more than 2% of account per trade",
        "✓ Follow your trading plan consistently",
        "✓ Keep emotions out of trading decisions",
        "✓ Review trades weekly for improvement",
        "✓ Consider market news and economic events",
        "✓ Use proper position sizing",
        "✓ Maintain trading journal"
    ]
    
    for item in advice:
        print(f"\033[1;92m✓ \033[1;97m{item}")
    
    print("\n\033[1;91m" + "⚠"*40)
    print("\033[1;91mDISCLAIMER: These are demo signals for educational purposes only.")
    print("\033[1;91mTrading involves risk. Past performance doesn't guarantee future results.")
    print("\033[1;91m" + "⚠"*40)
    
    # Save option
    save_option = input("\n\033[1;92mSave report to file? (y/n): ")
    if save_option.lower() == 'y':
        filename = f"trading_signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"TRADING SIGNALS REPORT\n")
                f.write(f"Generated: {current_time}\n")
                f.write(f"Trading Mode: {selected_mode['name']}\n")
                f.write(f"Timeframe: {selected_tf}\n")
                f.write(f"Account Size: ${account_size:,.2f}\n")
                f.write(f"Risk per Trade: {risk_percent}%\n\n")
                
                for signal in signals:
                    f.write(f"[{signal['pair']}]\n")
                    f.write(f"  Signal: {signal['signal']}\n")
                    f.write(f"  Confidence: {signal['confidence']}\n")
                    f.write(f"  Entry: {signal['entry']}\n")
                    f.write(f"  Target: {signal['target']}\n")
                    f.write(f"  Stop Loss: {signal['stop_loss']}\n")
                    f.write(f"  Risk/Reward: {signal['risk_reward']}\n\n")
                
                f.write("\nTRADING ADVICE:\n")
                for item in advice:
                    f.write(f"- {item}\n")
            
            print(f"\033[1;92mReport saved as: {filename}")
        except Exception as e:
            print(f"\033[1;91mError saving file: {e}")
    
    print("\n\033[1;92m" + "═"*60)
    print("\033[1;92m║\033[1;97m         THANK YOU FOR USING TRADING TOOLS          \033[1;92m║")
    print("\033[1;92m║\033[1;97m         Press Enter to exit the program           \033[1;92m║")
    print("\033[1;92m" + "═"*60)
    input()

if __name__ == "__main__":
    main()
