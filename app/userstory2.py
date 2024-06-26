# same imports
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config
from openai import OpenAI


client = OpenAI(api_key=Config.OPENAI_API_KEY)

# Define the guidelines text
guidelines_text = """
COMMUNITY FIRST HEALTH PLANS PCP MEDICAL RECORD DOCUMENTATION AND CONTINUITY GUIDELINES Community First has established guidelines for medical record documentation. Individual medical records for each family member are to be maintained. The medical records must be handled and maintained in a confidential manner and must be organized in such a manner that all progress notes, diagnostic tests, reports, letters, discharge summaries and other pertinent medical information are readily accessible. In addition, each office should have a written policy in place to ensure that medical records are safeguarded against loss, destruction, or unauthorized use. Criteria Requirements A. Documentation 1. Patient Identification Each page of the medical record must include a unique identifier, which may include patient identification number, medical record number, first and last name. 2. Personal Data Personal/biographical data including the age, sex, address, employer, home and work telephone numbers, marital status of the patient, and emergency ontacts must be included in the medical record. 3. Allergies Medication allergies and adverse reactions (including immunization reactions) should be prominently noted in the record. If the patient has no known allergies or history of adverse reactions, this should be appropriately noted in the record. 4. Problem List For patients seen three (3) or more times, a separate list of all the patient’s chronic/significant problems must be maintained. A chronic problem is defined as one that is of long duration, shows little change or is of slow progression. 5. Medication List For patients seen three (3) or more times, maintenance/ongoing medications should be listed on a medication sheet and updated as necessary with dosage changes and the date the change was made. A separate medication sheet is recommended but if a physician chooses to write out all current medications at each visit, this is acceptable. The medication list should include information/instruction to the member. 6. Chart Legible Medical records must be legible to someone other than the author. A record that is deemed illegible by the reviewer should be evaluated by a second person. 7. Author Signature All entries in the medical record must be signed by the author/performing provider. 8. Entries Dated Each and every entry must be accompanied by a date (month, day and year). 9. Advance Directive For medical records of Medicaid adults, 18 years and older, the medical record must document whether or not the individual has executed an advance directive. An advanced directive is a written instruction such as a living will or durable power of attorney for health care relating to the provision of health care when the individual is incapacitated. 2 http://www.uspreventiveservicestaskforce.org/uspstf/uspsrecsdate.htm, revised August 2020 B. CONTINUITY OF CARE 10. Past Medical History For patients seen three (3) or more times, a past medical history should be easily identified and should include serious accidents, operations, and illnesses. For children and adolescents (18 years and younger), past medical history should relate to prenatal care, birth, operations, and childhood illnesses. 11.Chief Complaint Every visit should have a notation identifying the current problem (significant illnesses, medical and behavioral health conditions and health maintenance concerns). 12.History And Physical Relevant To Chief Complaint The history and physical records should reflect appropriate subjective and objective information pertinent to the patient’s presenting complaints. 13. Working Diagnosis Consistent with Findings The diagnosis identified during each visit should be documented and should be consistent with findings. ICD-10 code(s) may be used but must include the written description of the diagnosis. 14. Basic Teaching Provided The medical record should reflect that the member is provided with basic teaching/instructions regarding their physical and/or behavioral health condition. 15. Appropriate Plan Of Treatment Based on the chief complaint, physical exam findings and diagnosis, the treatment plan should be clearly documented. 16. Appropriate Use Of Consultants If a patient problem occurs which is outside the physician’s scope of practice, there must be a referral to an appropriate specialist. 17. Appropriate Studies Ordered The laboratory and other studies ordered should be consistent with the treatment plan as related to the documented working diagnosis and should be documented at the time of the visit. Abnormal findings must have an explicit notation of follow-up plans. 18.Unresolved Problems From Previous Visits Addressed Documentation should reflect that the physician provides continuous evaluation of problems noted in previous visits. 19.MD Review Of Studies There must be evidence that the physician has reviewed the results of diagnostic studies. Methods can vary, but often the physician will initial the lab report or mention it in the progress notes. 20. Results Of Consultations When the patient is referred to another physician for consultation, there must be a copy of the results of the consult report and any associated diagnostic work-up in the medical record. Primary physician review of the consultation must be documented. Often the physician initials the consult report. 21. Date Of Next Visit Encounter forms or notes should have a notation, when indicated, regarding follow-up care, calls, or visits. Specific time of return should be noted in weeks, months, or as needed. 22. ER And Hospital Records Pertinent inpatient records must be maintained in the office medical record. These records may include but are not limited to the following: H&P, surgical procedure reports, authorizations, ER reports and hospital discharge summaries. For pediatric patients seen since birth, the labor and delivery records, including the newborn assessment, should be in the medical record. 3 http://www.uspreventiveservicestaskforce.org/uspstf/uspsrecsdate.htm, revised August 2020 23. Evidence That Patient Was Not Placed At Risk The record should reflect that the patient has not been placed at inappropriate risk by a diagnostic or therapeutic problem. 24. Evaluation for abuse / neglect or other socioenvironmental factors (Medicaid only) Medical records of Medicaid adults should reflect evidence that the provider evaluates for signs / symptoms or behaviors associated with abuse / neglect or other significant socioenvironmental factors. 25. Annual Reminders Annual reminders to be sent to members regarding preventive care, well child/annual physical 26. Diagnosis Validation The record should reflect that the billing diagnosis is consistent with that of the chief complaint. 27. Claims Validation The record should reflect the documented encounter is appropriate for the level of E/M services billed.
"""
def generate_targeted_questions(econsult_data, guidelines_text):
    """

    :param econsult_data: A string containing the eConsult data.
    :param guidelines_text: A string containing the standard eConsult guidelines.
    :return: A list of targeted questions.
    """
    messages = [{
        'role': 'user',
        'content': f"You are a Primary Care Provider and provided the standard eConsult guidelines and patient's consultation notes, I want you to generate a list of 3-4 MOST important targeted questions for the PCP to review and send over to the specialist for further diagnosis. Standard eConsult guidelines: {guidelines_text}, and patient's data: {econsult_data}"
    }]
    completion = client.chat.completions.create(
        max_tokens=1000,
        model="gpt-3.5-turbo",
        messages=messages
    )

    questions = completion.choices[0].message.content.strip()
    return questions
def main():
    user_input = """
    Patient Name: John Smith
    Date of Visit: 03/25/2023
    Chief Complaint: Shortness of breath and cough

    History of Present Illness:
    Mr. Smith presents today with complaints of shortness of breath and cough with yellow-green sputum production for the past week. He reports a fever of 101°F and chest pain that worsens with deep breathing or coughing.
    - Hypertension
    - Hyperlipidemia

    Medications:
    - Lisinopril 10mg daily
    - Atorvastatin 20mg daily

    Family History:
    - Father: Hypertension
    - Mother: Hyperlipidemia

    Social History:
    - Non-smoker
    - Rare alcohol use

    Physical Exam:
    - General: Appears ill, in moderate distress
    - Vital Signs: BP 140/90, HR 100, RR 24, Temp 101°F
    - Respiratory: Decreased breath sounds and crackles on the right lower lung field

    Assessment and Plan:
    1. Confirm diagnosis with chest X-ray
    2. Start empirical antibiotic therapy for community-acquired pneumonia
    3. Prescribe albuterol inhaler for bronchodilation
    4. Advise bed rest and adequate fluid intake
    5. Follow up in 3 days for reassessment
    """

    # Generate targeted questions based on the eConsult data
    targeted_questions = generate_targeted_questions(user_input, guidelines_text)
    return targeted_questions

if __name__ == "__main__":
    main()

