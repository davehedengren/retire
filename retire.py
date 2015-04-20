from __future__ import division
import datetime

def retire(assets=0, mSav = 4000, mRExp = 4000, ror=0.07):
    """
    Calculate when 4% of investments is greater than monthly expenditures
    (i.e. retirement) based on input assumptions
    assets: How much investiable money you have today (default = 0)
    mSav: How much money can you save each month (default = 1000)
    mRExp: How much money do you want in each month of retirement (default =
    2000)
    ror: Assumed return on investment (default = 0.07)
    """
    retire_assets = (mRExp * 12) / .04
    date = datetime.date.today()
    mror = ((1 + ror)**(1/12))-1
    while assets < retire_assets:
        assets = assets*(1+mror) + mSav
        date += datetime.timedelta(days=30)
        if date.month == 12:
            print('{:%Y}'.format(date), '${:11,.0f}'.format(assets))

    print('You can retire in','{:%b %Y}'.format(date),'with',
                 '${:11,.0f}'.format(assets))
