# answer to the ada academy assessment demo question
# Complete the 'subscription_summary' function below.
#


def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()
    
    # constants
    BUNDLE_COST = 18.0
    SINGLE_COST = 7.0
    AD_FREE_MONTH_COST = 2.0
    VIDEO_ON_DEMAND_COST = 27.99
    
    # variables
    accounts = {}  # account dictionary
    total_all = 0  # total earnings for all customers
    total_premium = 0  # total earned from ad-free and on-demand
    most_profitable = 0  # most profitable amount
    most_prof_accounts = [] # most profitable accounts
    n_accounts = len(months_subscribed)  # assuming three params have same length
    
    # populate dictionary and print result of each account
    for ind in range(n_accounts):
        # account index start from 1
        accounts[ind+1] = [
            (months_subscribed[ind]//3*BUNDLE_COST) + (months_subscribed[ind]%3*SINGLE_COST),
            ad_free_months[ind] * AD_FREE_MONTH_COST,
            video_on_demand_purchases[ind] * VIDEO_ON_DEMAND_COST,
            0
        ]
        
        # compute account info
        account_total = sum(accounts[ind+1])
        total_all += account_total
        total_premium += (accounts[ind+1][1] + accounts[ind+1][2])
        if account_total > most_profitable:
            most_profitable = account_total
        accounts[ind+1][3] = account_total
        
        # print account info
        print("Account {} made ${:.2f} total".format(ind+1, account_total))
        print(">>> ${:.2f} from monthly subscription fees".format(accounts[ind+1][0]))
        print(">>> ${:.2f} from Ad-free upgrades".format(accounts[ind+1][1]))
        print(">>> ${:.2f} from Video on Demand purchases\n".format(accounts[ind+1][2]))
    
    # print summary
    print("Combined all accounts made ${:.2f} total".format(total_all))
    print("Premium content (Ad-free watching and Video on Demand) made ${:.2f} total\n".format(total_premium))
    
    # compute and print most profitable customer
    for k, v in accounts.items():
        if v[3] >= most_profitable:
            most_prof_accounts.append('#{}'.format(k))
    print("${:.2f} was the most earned by any single account".format(most_profitable))
    print("The accounts that earned the most were:", ', '.join(most_prof_accounts))

    

if __name__ == '__main__':    
    months_subscribed = []
    ad_free_months = []
    video_on_demand_purchases = []
    
    header = input().strip()

    while header == "months_subscribed:":
        line = input().strip()
        try:
            months_subscribed.append(int(line))
        except ValueError:
            header = line

    while header == "ad_free_months:":
        line = input().strip()
        try:
            ad_free_months.append(int(line))
        except ValueError:
            header = line

    while header == "video_on_demand_purchases:":
        try:
            line = input().strip()

            video_on_demand_purchases.append(int(line))
        except EOFError:
            header = None
            
    subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)
