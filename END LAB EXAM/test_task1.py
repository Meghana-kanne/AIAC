
from task1 import summarize_clinical_note

class TestClinicalSummarizer(unittest.TestCase):

    def test_case_1(self):
        note = """Chief Complaint: Shortness of breath.
        History of Present Illness: 65-year-old male with 2 days of progressive dyspnea.
        Vitals: Temp 100.4 F, HR 110, BP 140/85, SpO2 92%.
        Assessment: Acute decompensated heart failure.
        Plan: Admit and start diuretics."""
        
        summary, text = summarize_clinical_note(note)
        
        self.assertIn("Chief Complaint", text)
        self.assertIn("Shortness of breath", text)
        self.assertIn("Plan:", text)

    def test_case_2(self):
        note = """Patient is a 29 yo female with recurrent headaches for 3 months.
        No known drug allergies. Impression: tension headache."""
        
        summary, text = summarize_clinical_note(note)
        
        self.assertIn("29 yo female", text)
        self.assertIn("tension", text)

    def test_case_3(self):
        note = """40M s/p MVC. PE: abdomen tender RUQ. Assessment: minor liver laceration."""
        
        summary, text = summarize_clinical_note(note)
        
        self.assertIn("liver laceration", text)
        self.assertIn("Assessment", text)


if __name__ == '__main__':
    unittest.main()
