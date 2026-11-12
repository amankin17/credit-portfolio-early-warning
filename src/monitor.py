"""Synthetic credit risk monitoring; not a validated lending decision system."""
import random, json
from collections import defaultdict

def generate_accounts(n=300,seed=17):
    rng=random.Random(seed)
    accounts=[]
    for i in range(1,n+1):
        product=rng.choice(['personal','auto','credit_card'])
        exposure=round(rng.uniform(1000,30000),2)
        dpd=rng.choices([0,15,30,45,60,90],[55,15,10,10,7,3])[0]
        util=round(rng.uniform(0.05,1.0),2)
        pti=round(rng.uniform(0.05,0.65),2)
        accounts.append({'account_id':i,'product':product,'exposure':exposure,'days_past_due':dpd,'utilisation':util,'payment_to_income':pti})
    return accounts

def flags(account):
    return [key for condition,key in [(account['days_past_due']>=30,'30_plus_dpd'),(account['utilisation']>=0.85,'high_utilisation'),(account['payment_to_income']>=0.45,'high_payment_burden')] if condition]

def summarise(accounts):
    groups=defaultdict(list)
    for a in accounts: groups[a['product']].append(a)
    summary={}
    for product,rows in sorted(groups.items()):
        total=len(rows)
        arrears=sum(a['days_past_due']>=30 for a in rows)
        flagged=sum(bool(flags(a)) for a in rows)
        summary[product]={'accounts':total,'exposure':round(sum(a['exposure'] for a in rows),2),'arrears_30_plus_rate':round(arrears/total,3),'flag_rate':round(flagged/total,3)}
    return summary
if __name__=='__main__':
    print(json.dumps(summarise(generate_accounts()),indent=2))
