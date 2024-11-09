def calculate_probabilities(prevalence, sensitivity, specificity):
    p_disease = prevalence
    p_test_positive_given_disease = sensitivity
    p_test_negative_given_no_disease = specificity
    p_no_disease = 1 - prevalence

    # Calculate the probability of a positive test result (P(Test+))
    p_positive_test_result = (prevalence * sensitivity) + (p_no_disease * (1 - specificity))
    
    # Calculate the probability of having the disease given a positive test result (P(Disease|Test+))
    if p_positive_test_result == 0:
        p_disease_given_positive_test = 0.0 
    else:
        p_disease_given_positive_test = (sensitivity * prevalence) / p_positive_test_result

    # Calculate the probability of a negative test result (P(Test-))
    p_negative_test_result = (prevalence * (1 - sensitivity)) + (p_no_disease * specificity)

    # Calculate the probability of having the disease given a negative test result (P(Disease|Test-))
    if p_negative_test_result == 0:
        p_disease_given_negative_test = 0.0 
    else:
        p_disease_given_negative_test = ((1 - sensitivity) * prevalence) / p_negative_test_result

    return p_disease_given_positive_test, p_disease_given_negative_test

def main():
    while True:
        try:
            prevalence = float(input("Enter the prevalence of the disease (e.g., 0.05 for 5%): "))
            sensitivity = float(input("Enter the sensitivity of the test (e.g., 0.9 for 90%): "))
            specificity = float(input("Enter the specificity of the test (e.g., 0.95 for 95%): "))

            prob_positive, prob_negative = calculate_probabilities(prevalence, sensitivity, specificity)

            print(f"\nProbability of disease given a positive test: {prob_positive:.4f}")
            print(f"Probability of disease given a negative test: {prob_negative:.4f}")

            break
        except ValueError:
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
