// The Manager1 class implements the following requirements:
// 1/ The system should validate the patient's age using defined limits and stop processing if the age is outside of the valid range. 
// 2/ The system should classify the patient's blood pressure (BP) reading as high risk (systolic BP > 150 and diastolic BP > 95), medium risk (systolic BP > 130), or normal. 
// 3/ The system should output the result for further processing.

import java.util.ArrayList;
import java.util.List;

public class Manager1 {

    private static final List<String> logs = new ArrayList<>();

    private static final int MIN_AGE = 0;
    private static final int MAX_AGE = 130;
    private static final int ADULT_AGE = 18;

    private static final int BP_SYS_HIGH_THRESHOLD = 150;
    private static final int BP_DIA_HIGH_THRESHOLD = 95;
    private static final int BP_SYS_MED_THRESHOLD = 130;
    private static final int BP_INVALID = 0;

    public enum RiskLevel {
        INVALID,
        NORMAL,
        MEDIUM,
        HIGH
    }

    public void validateAge(Patient1 patient) {
        if (patient.getAge() < MIN_AGE || patient.getAge() > MAX_AGE) {
            System.out.println("Invalid age!" + patient.getAge());
            logs.add("Invalid patient: " + patient.getName());
            return;
        }

        if (patient.getAge() < ADULT_AGE) {
            System.out.println("Patient is a minor.");
        } else {
            System.out.println("Patient is an adult.");
        }

        logs.add("Processed patient " + patient.getName());
    }

    public RiskLevel classifyBloodPressure(Patient1 patient, int bpSys, int bpDia, boolean printResult) {
        if (bpSys < BP_INVALID || bpDia < BP_INVALID) {
            logs.add("Invalid patient BbSys or bpDia value");
            return RiskLevel.INVALID;
        }

        RiskLevel result;

        // Requirement: high risk (systolic BP > 150 and diastolic BP > 95)
        if (bpSys > BP_SYS_HIGH_THRESHOLD && bpDia > BP_DIA_HIGH_THRESHOLD) {
            result = RiskLevel.HIGH;
        } else if (bpSys > BP_SYS_MED_THRESHOLD) {
            result = RiskLevel.MEDIUM;
        } else {
            result = RiskLevel.NORMAL;
        }

        if (printResult) {
            System.out.println("Patient " + patient.getName() + ": score=" + result);
        }

        return result;
    }
}

class Patient1 {
    private String name;
    private int age;
    private String existingCondition;

    public Patient1(String name, int age, String condition) {
        this.name = name;
        this.age = age;
        this.existingCondition = condition;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getExistingCondition() {
        return existingCondition;
    }
}
