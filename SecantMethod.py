def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    """
    Υλοποίηση της μεθόδου της Τέμνουσας για την εύρεση ριζών μιας συνάρτησης.

    :param f: Η συνάρτηση της οποίας θέλουμε να βρούμε τη ρίζα.
    :param x0: Η αρχική προσέγγιση 1.
    :param x1: Η αρχική προσέγγιση 2.
    :param tol: Το αποδεκτό όριο σφάλματος.
    :param max_iter: Ο μέγιστος αριθμός επαναλήψεων.
    :return: Η προσέγγιση της ρίζας.
    """
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Διαίρεση με το μηδέν, σταματά η εκτέλεση.")
            return None

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x2 - x1) < tol:
            print(f"Η ρίζα βρέθηκε μετά από {i+1} επαναλήψεις: x = {x2}")
            return x2

        x0, x1 = x1, x2
    
    print(f"Η ρίζα δεν βρέθηκε μετά από {max_iter} επαναλήψεις.")
    return None

# Παράδειγμα χρήσης
def f(x):
    return x**2 - 4

root = secant_method(f, 1, 2)
print("Προσέγγιση της ρίζας:", root)
