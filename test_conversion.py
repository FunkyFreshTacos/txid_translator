import unittest
from unittest.mock import patch
import io
import sys
from txid_translation import (
    DW10_Magnet, DW10_External, SMKT3, SMKT3_Heat, SMKT3_Freeze,
    GB1, PIR1, KEY2_PANIC1, FT1, FT1_Heat, FT1_Freeze,
    CO3, TILT1, HW_SHOCK
)

class TestTXIDTranslation(unittest.TestCase):
    def test_dw10_magnet_small(self):
        # payload_len < 5: hex(123) is '0x7b', len=2
        # new_hex = '0x' + '2' + '0' + '7b' = '0x207b' = 8315
        # final = '0160' + '8315' = '01608315'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            DW10_Magnet(123)
            self.assertIn("Translated TXID:  01608315", fake_out.getvalue())

    def test_dw10_magnet_large(self):
        # payload_len >= 5: hex(0x123456) is '0x123456', len=6
        # new_hex = '0x' + '2' + '123456' = '0x2123456' = 34747478
        # final = '0160' + '34747478' = '016034747478'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            DW10_Magnet(0x123456)
            self.assertIn("Translated TXID:  016034747478", fake_out.getvalue())

    def test_pir1_large(self):
        # payload_len >= 5: hex(1048576) is '0x100000', len=6
        # new_hex = '0x' + '0' + '100000' = '0x0100000' = 1048576
        # final = '0160' + '1048576' = '01601048576'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            PIR1(1048576)
            self.assertIn("Translated TXID:  01601048576", fake_out.getvalue())

    def test_dw10_external(self):
        # Small: hex(1) = '0x1', len=1 < 5
        # new_hex = '0x' + '2' + '0' + '1' = '0x201' = 513
        # final = '1120' + '513' = '1120513'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            DW10_External(1)
            self.assertIn("Translated TXID:  1120513", fake_out.getvalue())

    def test_key2_panic1_small(self):
        # len < 6: hex(0x12345) = '0x12345', len=5
        # new_hex = '0x' + '00' + '12345' = '0x0012345' = 74565
        # prefix = '0480'
        # final = '048074565'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            KEY2_PANIC1(0x12345)
            self.assertIn("Translated TXID:  048074565", fake_out.getvalue())

    def test_key2_panic1_large(self):
        # len >= 6: hex(0x123456) = '0x123456', len=6
        # new_hex = '0x' + '0' + '123456' = '0x0123456' = 1193046
        # prefix = '048'
        # final = '0481193046'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            KEY2_PANIC1(0x123456)
            self.assertIn("Translated TXID:  0481193046", fake_out.getvalue())

    def test_tilt1_small(self):
        # len < 5: hex(0x1234) = '0x1234', len=4
        # new_hex = '0x' + 'C0' + '1234' = '0xC01234' = 12587572
        # prefix = '1120'
        # final = '112012587572'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            TILT1(0x1234)
            self.assertIn("Translated TXID:  112012587572", fake_out.getvalue())

    def test_tilt1_large(self):
        # len >= 5: hex(0x12345) = '0x12345', len=5
        # new_hex = '0x' + 'C' + '12345' = '0xC12345' = 12657477
        # prefix = '112'
        # final = '11212657477'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            TILT1(0x12345)
            self.assertIn("Translated TXID:  11212657477", fake_out.getvalue())

    def test_smkt3_heat(self):
        # Small: hex(10) = '0xa', len=1
        # new_hex = '0x' + '9' + '0' + 'a' = '0x90a' = 2314
        # final = '1120' + '2314' = '11202314'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            SMKT3_Heat(10)
            self.assertIn("Translated TXID:  11202314", fake_out.getvalue())

    def test_hw_shock(self):
        # Large: hex(0xFFFFFF) = '0xffffff', len=6
        # new_hex = '0x' + '3' + 'ffffff' = '0x3ffffff' = 67108863
        # final = '1120' + '67108863' = '112067108863'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            HW_SHOCK(0xFFFFFF)
            self.assertIn("Translated TXID:  112067108863", fake_out.getvalue())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTXIDTranslation)
    result = unittest.TextTestResult(sys.stdout, True, 1)
    
    print("\n" + "="*40)
    print("      TXID Translation Test Summary")
    print("="*40)
    
    # We'll run the tests manually to get the pass/fail for each
    runner = unittest.TextTestRunner(stream=io.StringIO()) # suppress default output
    
    total_passed = 0
    total_failed = 0
    
    for test in suite:
        test_name = test._testMethodName
        res = unittest.TestResult()
        test.run(res)
        
        if res.wasSuccessful():
            status = "PASS"
            total_passed += 1
        else:
            status = "FAIL"
            total_failed += 1
            
        print(f"{test_name:<30} | {status}")

    print("-" * 40)
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    print("=" * 40 + "\n")
