import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from monitor import flags,generate_accounts,summarise
class MonitorTests(unittest.TestCase):
    def test_flags_at_boundaries(self):
        row={'days_past_due':30,'utilisation':0.85,'payment_to_income':0.45}
        self.assertEqual(len(flags(row)),3)
    def test_not_flagged(self):
        self.assertEqual(flags({'days_past_due':0,'utilisation':0.2,'payment_to_income':0.1}),[])
    def test_counts(self):
        r=generate_accounts(100)
        s=summarise(r)
        self.assertEqual(sum(v['accounts'] for v in s.values()),100)
        self.assertTrue(all(0<=v['arrears_30_plus_rate']<=1 for v in s.values()))
if __name__=='__main__': unittest.main()
